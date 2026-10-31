# UHF Antenna Design for LoRa Applications (Project FS04)

[![University](https://img.shields.io/badge/University-Cape%20Town%20(UCT)-blue.svg)](http://www.uct.ac.za/)
[![Department](https://img.shields.io/badge/Department-Electrical%20Engineering-orange.svg)](http://www.ee.uct.ac.za/)
[![Course](https://img.shields.io/badge/Course-EEE4022S%20Final%20Year%20Project-green.svg)]()
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)]()

> **Author:** Mpumelelo Ntuthuko Mpanza (`MPNMPU002`)
> **Supervisor:** Dr. Francois Willem Schonken  
> **Institution:** Department of Electrical Engineering, University of Cape Town 

---

## 📌 Project Overview

Antenna design at ultra high frequencies 300 MHz to 3 GHz presents significant physical constraints, particularly within the 433 MHz and 868 MHz ISM bands utilized by Long Range (LoRa) Internet of Things deployments. Traditional quarter wavelength resonant elements 173.1 mm at 433 MHz and 86.4 mm at 868 MHz are frequently too large for compact modern device enclosures.

Compressing physical dimensions below quarter wave pushes these radiators into the Electrically Small Antenna domain (ka < 0.5). According to the Chu-Harrington limit, spatial reduction leads to an exponential increase in stored reactive near field energy, resulting in narrow operational bandwidths, low radiation resistances, and high sensitivity to dielectric loading.

This repository contains the complete computational electromagnetic simulation models FEKO, KiCAD PCB layout files, mechanical designs and empirical test data for four specialized, pretuned compact antenna topologies designed to provide future UCT LoRa developers with easily integrable PCB drop in components.

---

## 🗂️ Repository Structure

```text
UHF-LoRa-Antenna-Design/
│
├── Coplannar IFA/              # 433 MHz Coplanar Inverted F Antenna (CADFEKO & KiCAD files)
├── Helical/                    # 433 MHz & 868 MHz Normal-Mode Helical Antennas & 3D print models
├── Quarter_Wave_Monopole/      # 868 MHz Meandered Monopole Antenna (CADFEKO & ground plane models)
├── Spiral/                     # 868 MHz Planar Archimedean Spiral Antenna (CADFEKO & PCB files)
└── .gitignore
