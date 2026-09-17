# Quantum Spectral Rigidity, Fock-Space Entanglement, and 5-Body Decoupling in the Prime-Phase Lattice

[![ORCID](https://img.shields.io/badge/ORCID-0009--0004--3627--6997-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0004-3627-6997)
[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.22804011-blue?logo=zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.22804011)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white&style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Research_Preprint-blue?style=flat-square)

> **"Microscopic Quantum Many-Body Dynamics of Riemann Zeros"**  
> Demonstrating GUE level repulsion, Fock-space entanglement phase transitions, and algebraic 5-body effective field theory decoupling along $\mathrm{Re}(s)=1/2$.

---

## Overview

This directory contains the official research manuscript and verification pipelines (`01`–`04`) for **Paper 2** of the K-Protocol framework. 

Extending the pairwise 2D interference spectroscopy established in Paper 1, this work formulates the microscopic multi-particle quantum dynamics of the prime-phase lattice. By mapping prime oscillators into a Fock-space generating polynomial framework, we verify that critical zeros emerge as quantum coherent resonance nodes exhibiting strict Gaussian Unitary Ensemble (GUE) level repulsion, entanglement entropy surges, and an algebraic 5-body interaction cutoff.

* **Paper 2 DOI (v1):** [10.5281/zenodo.22804011](https://doi.org/10.5281/zenodo.22804011)
* **Concept DOI (All Versions):** [10.5281/zenodo.22804010](https://doi.org/10.5281/zenodo.22804010)

---

## Key Scientific Findings

### 1. Microscopic GUE Level Repulsion (`01_gue_level_repulsion.py`)
* The nearest-neighbor spacing distribution $P(s)$ of the prime interference matrix reconstructs the Dyson-Montgomery GUE Wigner surmise:
  $$P(s) \approx \frac{32}{\pi^2} s^2 \exp\left(-\frac{4}{\pi} s^2\right)$$
* Eliminates Poissonian zero clustering ($P(0) = 0$) and confirms quadratic spectral rigidity ($s^2$ repulsion) driven directly by prime phase anti-correlations.

### 2. Fock-Space Entanglement Phase Transition (`02_fock_entanglement_transition.py`)
* Decomposing the 100-prime generating polynomial into bipartitions of Fock subspaces reveals a sharp **+21.6% Von Neumann entanglement entropy surge** precisely at the zero-crossing coordinate ($t_{100} \approx 236.5242$).
* Validates that non-trivial zeros represent macroscopic phase-locking transitions across microscopic oscillator states.

### 3. Algebraic N-Body Decoupling & 5-Body Cutoff (`03_nbody_algebraic_decoupling.py`)
* Multi-particle symmetric polynomial interactions satisfy an absolute algebraic bound:
  $$|S_{100}(t)| \le \prod_{j=1}^{100} \frac{1}{\sqrt{p_j}} = 1.4568 \times 10^{-110}$$
* Orders $k \le 5$ capture **99.8718% of total spectral energy**, proving that higher-order multiparticle fluctuations ($k \ge 6$) decouple exponentially and justifying a 5-body Effective Field Theory (EFT) truncation.

### 4. Sub-Critical Saturation Breakdown (`04_off_critical_stress_test.py`)
* Evaluating the 5-body saturation across coordinates $\sigma \in [0.20, 0.80]$ demonstrates that the 99.8% energy confinement is uniquely stable on the critical line $\sigma = 1/2$.
* When $\sigma < 1/2$, the saturation floor collapses rapidly (dropping below 76.5% at $\sigma = 0.20$), showing the catastrophic breakdown of the effective field theory off the critical axis.

---

## Repository Structure

```plaintext
02/
├── Prime_Phase_Interference_Riemann_Zeros2.pdf   # Complete Paper 2 research manuscript
├── 01_gue_level_repulsion.py                     # Pipeline 01: GUE level repulsion & spectral spacing
├── 01_gue_level_repulsion_analysis.png           # 4-panel diagnostic plot for Pipeline 01
├── 02_fock_entanglement_transition.py           # Pipeline 02: Fock-space Von Neumann entanglement entropy
├── 02_fock_entanglement_analysis.png             # 4-panel diagnostic plot for Pipeline 02
├── 03_nbody_algebraic_decoupling.py              # Pipeline 03: 5-body generating polynomial energy saturation
├── 03_nbody_algebraic_decoupling_analysis.png    # 4-panel diagnostic plot for Pipeline 03
├── 04_off_critical_stress_test.py                # Pipeline 04: Off-critical stability & saturation rupture
├── 04_off_critical_stress_test_analysis.png     # 4-panel diagnostic plot for Pipeline 04
├── requirements.txt                              # Python environment dependencies
├── LICENSE                                       # MIT License
└── README.md                                     # Directory documentation