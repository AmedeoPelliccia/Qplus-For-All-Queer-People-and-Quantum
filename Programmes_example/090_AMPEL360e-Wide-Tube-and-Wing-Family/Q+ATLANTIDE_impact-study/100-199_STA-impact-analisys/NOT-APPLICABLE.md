# STA Impact — Not Applicable for eWTW

**Programme:** 090_AMPEL360e-Wide-Tube-and-Wing-Family  
**Band:** 100-199_STA — Space Technology Architecture  
**Impact intensity:** · None  
**Status:** Not applicable at programme-band level  

## Rationale

The eWTW programme is a medium-range, full-electric / hybrid-electric atmospheric aircraft family. It does not operate in orbital, suborbital, cis-lunar, interplanetary, or space-infrastructure environments.

Therefore, STA 100–199 is not directly applicable to the eWTW programme baseline.

## STA range-by-range reading for eWTW

| STA range | Title                                       | eWTW impact    | Reason                                                        |
| --------- | ------------------------------------------- | -------------- | ------------------------------------------------------------- |
| `100-109` | Sistemas Generales y Soporte Vital Espacial | `·`            | No spacecraft general architecture or ECLSS                   |
| `110-119` | Estructuras y Materiales Espaciales         | `·`            | Aircraft structures stay under ATLAS 050–059 and AMTA 500–599 |
| `120-129` | Propulsión Espacial                         | `·`            | eWTW propulsion is atmospheric, under EPTA / ATLAS            |
| `130-139` | Sistemas de Energía Espacial                | `·`            | Aircraft energy systems stay under EPTA 400–499               |
| `140-149` | Aviónica y Control de Misión Espacial       | `·`            | Aircraft avionics stay under ATLAS 040–049 and DTCEC          |
| `150-159` | Comunicaciones Espaciales                   | `○ / optional` | Only if SATCOM is selected as a dedicated architecture item   |
| `160-169` | Sensores y Carga Útil Espacial              | `·`            | No space payload                                              |
| `170-179` | Operaciones y Mantenimiento en Órbita       | `·`            | No orbital servicing                                          |
| `180-189` | Infraestructura y Logística Espacial        | `·`            | No spaceport or orbital logistics baseline                    |
| `190-199` | Sistemas Avanzados y Futuro Espacial        | `·`            | Not part of eWTW baseline                                     |

## Programme matrix row

| **100-199 STA** | · | · | · | · | · | · | ◐ | ●●● | ●●● |

where:

```text
090 eWTW          = ·
095 GAIA-AIR      = ◐
096 PLUS-Q10      = ●●●
097 GAIA-SPACE QCCS = ●●●
```

## Controlled exception rule

STA cross-reference may be opened only if one of the following applies:

- space-derived avionics or GNC architecture is adopted;
- SATCOM architecture becomes programme-defining;
- radiation-hardening requirements are introduced beyond normal aviation environment assumptions;
- space-grade solar, battery, thermal, or optical-link technology is explicitly reused;
- eWTW becomes part of a spaceport, high-altitude, or orbital-support operational concept.

Until then, STA remains out of scope.

## Best controlled statement

For the 090_AMPEL360e-Wide-Tube-and-Wing-Family programme, STA 100–199 has no direct programme-band impact. Any space-domain influence shall be treated as external technology heritage or optional cross-reference, not as a controlled STA workstream, unless the programme baseline introduces SATCOM, radiation-hardening, space-derived energy systems, or spaceport/orbital-support operations.
