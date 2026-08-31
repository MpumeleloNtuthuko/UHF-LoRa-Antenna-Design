# Meandered Monopole Antenna

## Project

**FS04 – UHF Antenna Design for LoRa Applications**

This folder contains the CADFEKO 2026 design and simulation files for the **Meandered Monopole antenna** investigated as one of the primary compact antenna candidates for the project.

---

## Design Objective

The objective of this design is to investigate whether a meandered monopole can provide suitable operation within the required LoRa frequency range while significantly reducing the physical length required by a conventional monopole.

The meandered geometry increases the effective electrical length of the radiator by folding the conductive path into a compact physical area.

This makes the antenna particularly relevant to the project's requirement for an antenna that can potentially be integrated into a constrained enclosure or PCB-based system.

---

## Simulation Environment

- **Software:** Altair Feko / CADFEKO 2026
- **Post-processing:** POSTFEKO 2026
- **Simulation type:** Electromagnetic full-wave simulation
- **Target frequency:** Approximately 433 MHz

---

## Current Design Status

The meandered monopole has undergone initial design and optimisation.

The current design has demonstrated resonance within the general UHF region, but further optimisation is required before the antenna can be considered sufficiently matched to the intended operating frequency.

The current resonance is not yet centred directly on the desired approximately 433 MHz operating frequency.

In addition, the current S11 value at resonance remains relatively poor compared with the Inverted-F design.

---

## Current Performance

| Parameter | Current Result |
|---|---:|
| Target frequency | ~433 MHz |
| Resonant frequency | Requires further optimisation |
| S11 at resonance | Requires further optimisation |
| Matching | Poor / requires improvement |
| Status | Active optimisation |

---

## Current Problem

The primary issues with the current meandered monopole are:

1. **Resonant frequency**

   The current resonant frequency does not sit directly at the desired operating frequency.

2. **Impedance matching**

   The current S11 response indicates that the antenna is not sufficiently well matched at the desired operating frequency.

3. **Further geometry optimisation**

   The radiator geometry requires additional tuning to simultaneously move the resonance toward the target frequency and improve the input impedance match.

---

## Optimisation Strategy

Further optimisation will focus on parameters such as:

- Total electrical length of the meander
- Length of individual meander sections
- Spacing between meander sections
- Width/thickness of the conducting radiator
- Feed position
- Ground-plane dimensions
- Overall antenna dimensions

The effect of each parameter will be investigated through iterative CADFEKO simulations.

The general optimisation process is:

1. Establish the current baseline design.
2. Identify the current resonant frequency.
3. Compare the resonance with the target frequency.
4. Modify the geometry to shift the resonance.
5. Evaluate the resulting S11 response.
6. Adjust the feed and/or radiator geometry to improve impedance matching.
7. Repeat the simulation until an improved design is obtained.

---

## Comparison With Inverted-F Design

At the current stage of development, the Inverted-F antenna has produced a more satisfactory simulated result.

The Inverted-F currently resonates at approximately **435 MHz** with an S11 of approximately **-12 dB**.

The meandered monopole has not yet achieved the same level of optimisation and therefore remains an active area of development.

This does not eliminate the meandered monopole as a candidate. Further optimisation is required before its performance can be fairly compared with the Inverted-F design.

---

## Project Status

**Status: Active optimisation**

The current design provides a baseline from which further optimisation will be performed.

The immediate objective is to:

- Shift the resonant frequency toward the required operating frequency.
- Improve S11 at the target frequency.
- Maintain the compact physical form factor.
- Determine whether the resulting design provides a viable alternative to the Inverted-F antenna.

---

## Files

This folder contains the CADFEKO project files associated with the current Meandered Monopole design and electromagnetic simulation.

Additional optimisation iterations and simulation results will be added as development continues.
