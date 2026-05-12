"""Numerical dynamics for the Ampel Theoretical Framework under SICO.CA doctrine."""

from __future__ import annotations

import numpy as np
from dataclasses import dataclass, field
from typing import Callable, Dict, Tuple


@dataclass
class SICOCAConstraints:
    """
    Restricciones operativas bajo doctrina SICO.CA.

    La operación solo mantiene plena eficacia si las externalidades
    permanecen por debajo de la capacidad regenerativa.
    """

    regeneration_capacity: float = 1.0
    auditability_threshold: float = 0.95
    equity_floor: float = 0.30
    lambda_penalty: float = 0.10

    def authorization_factor(self, externalities: float) -> float:
        """Calcula chi_SICOCA como penalización continua."""
        violation = max(0.0, externalities - self.regeneration_capacity)
        return float(np.exp(-self.lambda_penalty * violation))

    def violation_magnitude(self, externalities: float) -> float:
        """Magnitud de violación de capacidad regenerativa."""
        return max(0.0, externalities - self.regeneration_capacity)


@dataclass
class AmpelDynamics:
    """
    Sistema acoplado I_EU, E_tech, D_ID con restricciones SICO.CA.

    Variables de estado:
        X[0] = I_EU   : integración europea
        X[1] = E_tech : eficacia tecnológica
        X[2] = D_ID   : adopción de identidad digital
    """

    # Coeficientes estructurales de integración
    a: float = 0.05
    b: float = 0.08
    c: float = 0.04
    d: float = 0.01

    # Elasticidades tecnológicas
    alpha: float = 0.60
    beta: float = 0.40

    # Coeficientes logísticos de identidad digital
    u: float = 1.20
    v: float = 0.80
    w: float = 1.00
    x: float = -2.50

    # Tasas de decaimiento y ajuste
    gamma_I: float = 0.02
    delta_E: float = 0.03
    sigma_D: float = 0.10

    # Acoplamientos cruzados
    kappa_EI: float = 0.02
    kappa_DE: float = 0.015
    eta_E: float = 0.50

    # Restricciones doctrinales
    constraints: SICOCAConstraints = field(default_factory=SICOCAConstraints)

    def logistic_adoption(self, I_EU: float, S: float, E_tech: float) -> float:
        """Objetivo logístico de adopción de identidad digital."""
        z = self.u * I_EU + self.v * S + self.w * E_tech + self.x
        return float(1.0 / (1.0 + np.exp(-z)))

    def derivatives(
        self,
        t: float,
        X: np.ndarray,
        inputs: Dict[str, Callable[[float], float]],
    ) -> np.ndarray:
        """
        Calcula las derivadas del sistema en el instante t.

        Parameters
        ----------
        t:
            Tiempo actual.
        X:
            Vector de estado ``[I_EU, E_tech, D_ID]``.
        inputs:
            Señales exógenas indexadas por nombre.  Las claves reconocidas son
            ``C``, ``R``, ``A_inst``, ``U``, ``A_adopt``, ``S`` y
            ``externalities``.  Las señales omitidas caen al valor por defecto
            documentado a continuación.

        Returns
        -------
        np.ndarray
            Vector ``[dI_EU/dt, dE_tech/dt, dD_ID/dt]``.
        """
        I_EU, E_tech, D_ID = X

        C = inputs.get("C", lambda _: 0.50)(t)
        R = inputs.get("R", lambda _: 0.60)(t)
        A_inst = inputs.get("A_inst", lambda _: 0.40)(t)
        U = inputs.get("U", lambda _: 0.70)(t)
        A_adopt = inputs.get("A_adopt", lambda _: 0.50)(t)
        S = inputs.get("S", lambda _: 0.80)(t)
        externalities = inputs.get("externalities", lambda _: 0.30)(t)

        chi = self.constraints.authorization_factor(externalities)

        dI_dt = (
            self.a * C
            + self.b * R
            + self.c * A_inst
            + self.d
            - self.gamma_I * I_EU
            + self.kappa_EI * E_tech
        )

        base_tech_growth = (
            self.eta_E
            * (U * A_adopt) ** self.alpha
            * max(I_EU, 0.0) ** self.beta
        )
        dE_dt = chi * base_tech_growth - self.delta_E * E_tech + self.kappa_DE * D_ID

        target_D = self.logistic_adoption(I_EU, S, E_tech)
        dD_dt = self.sigma_D * (target_D - D_ID)

        return np.array([dI_dt, dE_dt, dD_dt], dtype=float)


def integrate_euler(
    model: AmpelDynamics,
    X0: np.ndarray,
    t_span: np.ndarray,
    inputs: Dict[str, Callable[[float], float]],
    enforce_domain: bool = True,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Integrador de Euler explícito con registro de violaciones SICO.CA.

    Parameters
    ----------
    model:
        Instancia de :class:`AmpelDynamics`.
    X0:
        Condición inicial ``[I_EU, E_tech, D_ID]``.
    t_span:
        Array de instantes de tiempo uniformemente espaciados.
    inputs:
        Señales exógenas (ver :meth:`AmpelDynamics.derivatives`).
    enforce_domain:
        Si ``True``, los estados se recortan a ``[0, 1]`` en cada paso.

    Returns
    -------
    X : np.ndarray, shape (len(t_span), 3)
        Trayectorias de estado.
    violations : np.ndarray, shape (len(t_span),)
        Magnitud de violación de capacidad regenerativa en cada paso.
    """
    X = np.zeros((len(t_span), 3), dtype=float)
    violations = np.zeros(len(t_span), dtype=float)
    X[0] = np.clip(X0, 0.0, 1.0)

    ext_fn = inputs.get("externalities", lambda _: 0.30)

    for i in range(len(t_span) - 1):
        dt = t_span[i + 1] - t_span[i]
        dX = model.derivatives(t_span[i], X[i], inputs)
        X[i + 1] = X[i] + dt * dX
        violations[i] = model.constraints.violation_magnitude(ext_fn(t_span[i]))

        if enforce_domain:
            X[i + 1] = np.clip(X[i + 1], 0.0, 1.0)

    # Record violation at the final timestep
    violations[-1] = model.constraints.violation_magnitude(ext_fn(t_span[-1]))

    return X, violations
