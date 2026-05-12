"""Tests for the Ampel numerical dynamics layer (SICO.CA sections 9.1–9.3)."""

import numpy as np
import pytest

from sicoca import AmpelDynamics, SICOCAConstraints, integrate_euler


# ---------------------------------------------------------------------------
# SICOCAConstraints
# ---------------------------------------------------------------------------


class TestSICOCAConstraints:
    def test_default_parameters(self):
        c = SICOCAConstraints()
        assert c.regeneration_capacity == 1.0
        assert c.auditability_threshold == 0.95
        assert c.equity_floor == 0.30
        assert c.lambda_penalty == 0.10

    def test_authorization_factor_no_violation(self):
        c = SICOCAConstraints(regeneration_capacity=1.0, lambda_penalty=0.10)
        # externalities below capacity → zero violation → factor == 1
        assert c.authorization_factor(0.5) == pytest.approx(1.0)
        assert c.authorization_factor(1.0) == pytest.approx(1.0)

    def test_authorization_factor_with_violation(self):
        c = SICOCAConstraints(regeneration_capacity=1.0, lambda_penalty=0.10)
        # externalities = 1.5 → violation = 0.5 → exp(-0.10 * 0.5)
        expected = float(np.exp(-0.10 * 0.5))
        assert c.authorization_factor(1.5) == pytest.approx(expected)

    def test_authorization_factor_is_between_zero_and_one(self):
        c = SICOCAConstraints(regeneration_capacity=1.0, lambda_penalty=0.10)
        for ext in np.linspace(0.0, 5.0, 20):
            factor = c.authorization_factor(ext)
            assert 0.0 < factor <= 1.0

    def test_authorization_factor_decays_with_violation(self):
        c = SICOCAConstraints(regeneration_capacity=1.0, lambda_penalty=0.10)
        assert c.authorization_factor(1.5) < c.authorization_factor(1.1)

    def test_violation_magnitude_no_violation(self):
        c = SICOCAConstraints(regeneration_capacity=1.0)
        assert c.violation_magnitude(0.8) == pytest.approx(0.0)
        assert c.violation_magnitude(1.0) == pytest.approx(0.0)

    def test_violation_magnitude_with_violation(self):
        c = SICOCAConstraints(regeneration_capacity=1.0)
        assert c.violation_magnitude(1.3) == pytest.approx(0.3)

    def test_custom_regeneration_capacity(self):
        c = SICOCAConstraints(regeneration_capacity=0.5, lambda_penalty=0.20)
        # externalities = 0.7 → violation = 0.2 → exp(-0.20 * 0.2)
        expected = float(np.exp(-0.20 * 0.2))
        assert c.authorization_factor(0.7) == pytest.approx(expected)


# ---------------------------------------------------------------------------
# AmpelDynamics — logistic_adoption
# ---------------------------------------------------------------------------


class TestLogisticAdoption:
    def test_output_is_between_zero_and_one(self):
        model = AmpelDynamics()
        for i_eu in np.linspace(0.0, 1.0, 5):
            for e_tech in np.linspace(0.0, 1.0, 5):
                result = model.logistic_adoption(i_eu, S=0.8, E_tech=e_tech)
                assert 0.0 < result < 1.0

    def test_logistic_increases_with_integration(self):
        model = AmpelDynamics()
        low = model.logistic_adoption(0.1, S=0.8, E_tech=0.5)
        high = model.logistic_adoption(0.9, S=0.8, E_tech=0.5)
        assert high > low

    def test_logistic_increases_with_tech_efficacy(self):
        model = AmpelDynamics()
        low = model.logistic_adoption(0.5, S=0.8, E_tech=0.1)
        high = model.logistic_adoption(0.5, S=0.8, E_tech=0.9)
        assert high > low


# ---------------------------------------------------------------------------
# AmpelDynamics — derivatives
# ---------------------------------------------------------------------------


_EMPTY_INPUTS: dict = {}  # triggers all built-in defaults in derivatives()


class TestDerivatives:
    def test_returns_array_of_length_3(self):
        model = AmpelDynamics()
        X = np.array([0.20, 0.15, 0.10])
        dX = model.derivatives(0.0, X, _EMPTY_INPUTS)
        assert dX.shape == (3,)
        assert dX.dtype == float

    def test_d_id_converges_toward_logistic_target(self):
        """D_ID derivative should be positive when D_ID is below logistic target."""
        model = AmpelDynamics()
        # High I_EU and E_tech push logistic target above 0.10
        X = np.array([0.80, 0.80, 0.10])
        dX = model.derivatives(0.0, X, _EMPTY_INPUTS)
        assert dX[2] > 0.0

    def test_e_tech_penalized_when_externalities_exceed_capacity(self):
        """Technology growth must be lower when externalities violate capacity."""
        model = AmpelDynamics(delta_E=0.0, kappa_DE=0.0)
        X = np.array([0.50, 0.0, 0.0])

        inputs_safe = {"externalities": lambda _: 0.50}
        inputs_violated = {"externalities": lambda _: 2.00}

        dX_safe = model.derivatives(0.0, X, inputs_safe)
        dX_violated = model.derivatives(0.0, X, inputs_violated)
        assert dX_safe[1] > dX_violated[1]

    def test_i_eu_grows_with_cooperation(self):
        model = AmpelDynamics(gamma_I=0.0, kappa_EI=0.0)
        X = np.array([0.0, 0.0, 0.0])
        low_C = {"C": lambda _: 0.10}
        high_C = {"C": lambda _: 0.90}
        assert model.derivatives(0.0, X, high_C)[0] > model.derivatives(0.0, X, low_C)[0]

    def test_zero_i_eu_does_not_raise(self):
        """I_EU = 0 should not cause a domain error in the power function."""
        model = AmpelDynamics()
        X = np.array([0.0, 0.10, 0.10])
        dX = model.derivatives(0.0, X, _EMPTY_INPUTS)
        assert np.all(np.isfinite(dX))


# ---------------------------------------------------------------------------
# integrate_euler
# ---------------------------------------------------------------------------


class TestIntegrateEuler:
    def _default_inputs(self):
        t_span = np.linspace(0.0, 10.0, 100)
        rng = np.random.default_rng(seed=42)
        noise = rng.normal(0.0, 0.02, size=len(t_span))
        externalities_series = 0.25 + 0.10 * np.sin(0.03 * t_span) + noise

        def externalities(t):
            idx = min(int(t / t_span[-1] * (len(t_span) - 1)), len(t_span) - 1)
            return float(externalities_series[idx])

        inputs = {
            "C": lambda t: 0.50 + 0.10 * np.sin(0.02 * t),
            "R": lambda t: 0.60 + 0.05 * t / 10.0,
            "A_inst": lambda t: 0.40 + 0.10 * (1.0 - np.exp(-0.02 * t)),
            "U": lambda t: 0.70 + 0.20 * (1.0 - np.exp(-0.03 * t)),
            "A_adopt": lambda t: 0.50 + 0.15 * (1.0 - np.exp(-0.025 * t)),
            "S": lambda t: 0.80,
            "externalities": externalities,
        }
        return t_span, inputs

    def test_output_shapes(self):
        model = AmpelDynamics()
        X0 = np.array([0.20, 0.15, 0.10])
        t_span, inputs = self._default_inputs()
        X, violations = integrate_euler(model, X0, t_span, inputs)
        assert X.shape == (len(t_span), 3)
        assert violations.shape == (len(t_span),)

    def test_initial_condition_preserved(self):
        model = AmpelDynamics()
        X0 = np.array([0.20, 0.15, 0.10])
        t_span, inputs = self._default_inputs()
        X, _ = integrate_euler(model, X0, t_span, inputs)
        np.testing.assert_array_almost_equal(X[0], np.clip(X0, 0.0, 1.0))

    def test_enforce_domain_clips_states(self):
        model = AmpelDynamics()
        X0 = np.array([0.20, 0.15, 0.10])
        t_span, inputs = self._default_inputs()
        X, _ = integrate_euler(model, X0, t_span, inputs, enforce_domain=True)
        assert np.all(X >= 0.0)
        assert np.all(X <= 1.0)

    def test_no_domain_enforcement_allows_values_outside_unit_interval(self):
        """With enforce_domain=False large inputs can push states out of [0,1]."""
        model = AmpelDynamics(a=10.0, b=10.0, c=10.0, d=10.0, gamma_I=0.0)
        X0 = np.array([0.20, 0.15, 0.10])
        t_span = np.linspace(0.0, 5.0, 50)
        X, _ = integrate_euler(model, X0, t_span, {}, enforce_domain=False)
        # With large coefficients and no clipping at least one state must exceed 1
        assert np.any(X > 1.0)

    def test_violations_are_non_negative(self):
        model = AmpelDynamics()
        X0 = np.array([0.20, 0.15, 0.10])
        t_span, inputs = self._default_inputs()
        _, violations = integrate_euler(model, X0, t_span, inputs)
        assert np.all(violations >= 0.0)

    def test_violations_zero_when_externalities_below_capacity(self):
        model = AmpelDynamics()
        X0 = np.array([0.20, 0.15, 0.10])
        t_span = np.linspace(0.0, 5.0, 50)
        # externalities always at 0.5, regeneration_capacity default 1.0
        inputs = {"externalities": lambda _: 0.50}
        _, violations = integrate_euler(model, X0, t_span, inputs)
        np.testing.assert_array_equal(violations, 0.0)

    def test_final_timestep_violation_is_recorded(self):
        """violations[-1] must reflect externalities at the last timestep."""
        model = AmpelDynamics()
        X0 = np.array([0.20, 0.15, 0.10])
        t_span = np.linspace(0.0, 5.0, 20)
        # Externalities well above capacity at all times
        inputs = {"externalities": lambda _: 2.0}
        _, violations = integrate_euler(model, X0, t_span, inputs)
        # The last entry must be non-zero (capacity = 1.0, ext = 2.0 → violation 1.0)
        assert violations[-1] == pytest.approx(1.0)

    def test_reproducibility_with_same_seed(self):
        """Two runs with the same seed and parameters must produce identical results."""
        model = AmpelDynamics(x=-2.5, u=1.2, w=1.0, beta=0.4, kappa_EI=0.02)
        t_span = np.linspace(0.0, 150.0, 3000)
        rng = np.random.default_rng(seed=42)
        noise = rng.normal(0.0, 0.02, size=len(t_span))
        externalities_series = 0.25 + 0.10 * np.sin(0.03 * t_span) + noise

        def make_inputs():
            def ext(t):
                idx = min(int(t / t_span[-1] * (len(t_span) - 1)), len(t_span) - 1)
                return float(externalities_series[idx])

            return {
                "C": lambda t: 0.50 + 0.10 * np.sin(0.02 * t),
                "R": lambda t: 0.60 + 0.05 * t / 150.0,
                "A_inst": lambda t: 0.40 + 0.10 * (1.0 - np.exp(-0.02 * t)),
                "U": lambda t: 0.70 + 0.20 * (1.0 - np.exp(-0.03 * t)),
                "A_adopt": lambda t: 0.50 + 0.15 * (1.0 - np.exp(-0.025 * t)),
                "S": lambda t: 0.80,
                "externalities": ext,
            }

        X0 = np.array([0.20, 0.15, 0.10])
        X1, v1 = integrate_euler(model, X0, t_span, make_inputs())
        X2, v2 = integrate_euler(model, X0, t_span, make_inputs())
        np.testing.assert_array_equal(X1, X2)
        np.testing.assert_array_equal(v1, v2)
