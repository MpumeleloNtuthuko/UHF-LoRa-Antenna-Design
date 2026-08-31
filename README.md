# UHF Antenna Design for LoRa Applications

## Project Overview

This repository contains the CADFEKO models and simulation results
for candidate UHF antennas being investigated for LoRa applications.

The project investigates compact antenna geometries suitable for
integration into the mechanical enclosure of the target system.

## Target Requirements

- Target LoRa frequency: approximately 433 MHz
- Target operating region: approximately 432–436 MHz
- Compact physical form factor
- Antenna suitable for integration into the target enclosure
- Initial focus on low-profile / compact antenna geometries

## Candidate Antennas

### 1. Meandered Monopole

The meandered monopole is being investigated as a compact antenna
configuration capable of providing the required electrical length
while reducing the physical height of the radiator.

Current preliminary result:

- Simulated resonance: approximately 420 MHz
- S11 at resonance: approximately -4.39 dB
- Status: Requires further impedance and frequency optimisation

### 2. Inverted-F Antenna

An inverted-F antenna is being investigated as a second candidate
for comparison with the meandered monopole.

Current status:

- Initial CADFEKO model created
- Simulation and optimisation in progress

## Simulation Software

- Altair Feko 2026
- CADFEKO
- POSTFEKO

## Repository Structure

- `designs/` – CADFEKO antenna models
- `results/` – simulation results and plots
- `documentation/` – requirements and simulation notes

## Current Work

The immediate objective is to:

1. Shift the meandered monopole resonance toward 433 MHz.
2. Improve the impedance match.
3. Complete the initial inverted-F simulation.
4. Compare S11 responses of the candidate antennas.
5. Investigate radiation characteristics and gain after achieving
   acceptable impedance matching.
