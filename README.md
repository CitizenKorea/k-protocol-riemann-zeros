# K-Protocol: Prime Phase Interference & Quantum Many-Body Dynamics of Riemann Zeros

[![ORCID](https://img.shields.io/badge/ORCID-0009--0004--3627--6997-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0004-3627-6997)
[![Paper 1 DOI](https://img.shields.io/badge/Paper_1_DOI-10.5281%2Fzenodo.22763956-blue?logo=zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.22763956)
[![Paper 2 DOI](https://img.shields.io/badge/Paper_2_DOI-10.5281%2Fzenodo.22804011-blue?logo=zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.22804011)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white&style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Research_Preprint-blue?style=flat-square)

> **"Deconstructing Critical Zeros into Unitary Prime Oscillators and Quantum Many-Body Rigidity"**  
> An open-science research framework characterizing non-trivial zeros of the Riemann zeta function through microscopic prime-phase spectroscopy, quantum chaos, and effective field theory (EFT) decoupling along the critical line $\mathrm{Re}(s)=1/2$.

---

## Repository Structure & Research Roadmap

This repository is organized into independent, sequential research modules corresponding to each stage of the K-Protocol framework:

| Directory | Research Scope & Focus | Key Deliverables & Pipelines | Zenodo Record |
| :--- | :--- | :--- | :--- |
| [**`01/`**](./01) | **Paper 1: Prime Phase Interference Spectroscopy**<br>Pairwise 2D destructive interference, Selberg resonance trenches, and Riemann-Siegel baseline calibration across 200 consecutive zeros. | • Complete Paper 1 Manuscript (`.pdf`)<br>• `k_protocol_master.py` (2D Tensor survey)<br>• `prime_resonance_radar.py` (Resonance trenches)<br>• 1,000-record benchmark datasets (`.csv`) | [![DOI](https://img.shields.io/badge/Zenodo-10.5281%2Fzenodo.22763956-blue?logo=zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.22763956) |
| [**`02/`**](./02) | **Paper 2: Quantum Many-Body Rigidity & 5-Body Decoupling**<br>Fock-space multiparticle generating polynomials, GUE level repulsion ($s^2$ rigidity), entanglement phase transitions, and sub-critical breakdown. | • Complete Paper 2 Manuscript (`.pdf`)<br>• `01_gue_level_repulsion.py` (GUE Wigner surmise)<br>• `02_fock_entanglement_transition.py` (+21.6% surge)<br>• `03_nbody_algebraic_decoupling.py` (99.8% saturation)<br>• `04_off_critical_stress_test.py` (Off-line breakdown) | [![DOI](https://img.shields.io/badge/Zenodo-10.5281%2Fzenodo.22804011-blue?logo=zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.22804011) |

---

## Core Scientific Highlights

1. **Pairwise 2D Phase Spectroscopy (Paper 1):**  
   Resolves the modulus squared $|P(1+it)|^2$ into an exact hyperbolic amplitude envelope $A_{pq} = 2/(pq)$[cite: 6]. Proves that low-frequency primes ($p, q \le 7$) govern 85.5% of destructive phase resonance leaders across critical zeros[cite: 6].
2. **GUE Spectral Rigidity from Microscopic Primes (Paper 2):**  
   Demonstrates that nearest-neighbor spacing distributions $P(s)$ derived purely from prime interference matrices converge directly to Dyson-Montgomery GUE level repulsion ($P(0)=0$), ruling out Poissonian clustering.
3. **Fock-Space Entanglement Phase Transition (Paper 2):**  
   Identifies a sharp +21.6% surge in Von Neumann entanglement entropy across bipartite Fock subspaces at exact zero crossings, characterizing critical zeros as macroscopic phase-locking transitions.
4. **Effective 5-Body Decoupling Floor (Paper 2):**  
   Establishes that interaction orders $k \le 5$ saturate $>99.8\%$ of total multiparticle energy on $\sigma = 1/2$, while off-critical shifts ($\sigma < 1/2$) trigger severe sub-critical energy divergence.

---

## Quick Start & Reproduction

Each directory maintains an independent virtual environment specification and execution workflow.

### Running Paper 1 Pipelines
```bash
cd 01
pip install -r requirements.txt
python k_protocol_master.py
python prime_resonance_radar.py
