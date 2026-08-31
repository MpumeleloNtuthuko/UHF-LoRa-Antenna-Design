# Inverted-F Antenna (IFA)

## Project

**FS04 – UHF Antenna Design for LoRa Applications**

This folder contains the CADFEKO 2026 design and simulation files for the **Inverted-F Antenna (IFA)** investigated as a compact antenna solution for the project.

---

## Design Objective

The objective of this design is to investigate and optimise an Inverted-F antenna for operation around the required LoRa operating frequency while maintaining a compact physical form factor suitable for integration into the intended enclosure.

The Inverted-F configuration was selected as one of the primary antenna candidates because its folded radiator structure allows the electrical length of the antenna to be increased without requiring a physically long straight radiator.

---

## Simulation Environment

- **Software:** Altair Feko / CADFEKO 2026
- **Post-processing:** POSTFEKO 2026
- **Simulation type:** Electromagnetic full-wave simulation
- **Target frequency:** Approximately 433 MHz
- **Current design frequency:** Approximately 435 MHz

---

## Current Design Status

The Inverted-F antenna has undergone initial geometry optimisation.

The current simulation produces a resonance at approximately:

**435 MHz**

with an S11 (reflection coefficient) of approximately:

**-12 dB**

The current result indicates that the antenna is reasonably well matched around the intended operating frequency.

The resonant frequency is also sufficiently close to the project's approximate 433 MHz target to make the current design a promising candidate for further consideration.

---

## Current Performance

| Parameter | Current Result |
|---|---:|
| Resonant frequency | ~435 MHz |
| S11 at resonance | ~-12 dB |
| Target frequency | ~433 MHz |
| Matching | Reasonable |
| Status | Optimised / promising candidate |

---

## Interpretation

The current result suggests that the Inverted-F antenna is capable of achieving resonance close to the required LoRa operating region while maintaining a relatively compact geometry.

An S11 of approximately -12 dB indicates that a significant portion of the incident power is being accepted by the antenna rather than being reflected back toward the source.

The design is therefore considered to have achieved a satisfactory initial optimisation result.

Further optimisation may still be possible, particularly if improved matching or closer alignment with the exact target frequency is required.

---

## Optimisation Considerations

Potential parameters that may be investigated during further optimisation include:

- Radiator length
- Folded section dimensions
- Shorting section position
- Feed position
- Radiator width
- Ground-plane dimensions
- Distance between the radiator and ground plane

Changes to these parameters can influence the resonant frequency and input impedance of the antenna.

---

## Project Status

**Status: Initial optimisation completed**

The current Inverted-F design is considered a successful candidate based on its present simulated resonance and S11 performance.

The design will be retained for comparison with the other antenna candidates and may proceed to further analysis and/or physical prototyping depending on the final project requirements.

---

## Files

This folder contains the CADFEKO project files associated with the current Inverted-F antenna design and its electromagnetic simulation.

Simulation results and additional design iterations will be added as the project progresses.
