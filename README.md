# UHF Antenna Design for LoRa Applications

## Overview

This repository contains the design, simulation, and optimisation work for a final-year engineering project investigating compact UHF antenna configurations for LoRa applications.

The project focuses on developing antenna designs that can operate around the 433 MHz LoRa frequency while maintaining a compact physical form factor suitable for integration into the intended system enclosure.

The antenna candidates are being designed and evaluated using **Altair Feko 2026**, primarily through **CADFEKO** for electromagnetic modelling and **POSTFEKO** for analysis of simulation results.

---

## Project Objectives

The primary objective of this project is to investigate and develop a compact antenna suitable for LoRa communication around the 433 MHz operating frequency.

The investigation focuses on:

- Designing compact UHF antenna geometries.
- Simulating the antenna candidates using CADFEKO.
- Evaluating the input reflection coefficient (S11).
- Shifting the resonant frequency toward the required operating frequency.
- Improving impedance matching.
- Investigating antenna bandwidth.
- Evaluating radiation characteristics and gain.
- Comparing different antenna configurations.
- Identifying a suitable antenna configuration for eventual physical implementation and measurement.

---

## Target Requirements

The current design target is based on the requirements discussed for the LoRa application.

| Parameter | Target |
|---|---|
| Application | LoRa |
| Target frequency | ~433 MHz |
| Operating region | Approximately 432–436 MHz |
| Antenna type | Compact UHF antenna |
| Primary performance parameter | S11 / impedance matching |
| Additional parameters | Bandwidth, radiation pattern, gain |
| Simulation software | Altair Feko 2026 |

The antenna geometry may be modified during optimisation to achieve the required electromagnetic performance while remaining compatible with the available physical space.

---

# Antenna Candidates

Two antenna configurations are currently being investigated.

## 1. Meandered Monopole

The meandered monopole is being investigated as a compact alternative to a conventional monopole.

The conductor is folded into a meandered path, increasing the electrical path length while reducing the physical height required by the radiator.

This configuration is particularly useful when the available physical space is limited.

### Current simulation status

The initial meandered monopole model has produced a clear resonance in the UHF frequency range.

The current iteration has approximately:

- Resonant frequency: **~420 MHz**
- S11 at resonance: **~−4.39 dB**
- Target frequency: **~433 MHz**

The current resonance is relatively close to the target frequency, but further optimisation is required to:

1. Shift the resonance toward 433 MHz.
2. Improve the impedance match.
3. Evaluate the resulting bandwidth.
4. Evaluate the radiation characteristics.

The current model is therefore considered an **initial design iteration**, rather than a final optimised antenna.

---

## 2. Inverted-F Antenna

An inverted-F antenna is being investigated as a second compact antenna configuration.

The inverted-F configuration provides another approach to achieving the required electrical length within a restricted physical form factor.

The design will be simulated and subsequently compared with the meandered monopole.

The comparison will consider parameters including:

- Resonant frequency.
- S11.
- Impedance matching.
- Bandwidth.
- Radiation pattern.
- Gain.
- Physical dimensions.
- Suitability for integration into the intended enclosure.

---

# Simulation Workflow

The current simulation workflow is:

```text
Antenna Requirements
        ↓
Antenna Geometry
        ↓
CADFEKO Model
        ↓
Material / Ground / Feed Definition
        ↓
Mesh
        ↓
FEKO Solver
        ↓
POSTFEKO
        ↓
S11 Analysis
        ↓
Geometry Optimisation
        ↓
Radiation / Gain Analysis
        ↓
Candidate Comparison
        ↓
Physical Prototype
        ↓
Measurement
