# K-Protocol: Unified Operator Theory & Superconductor Inverse Design Suite

[![ORCID](https://img.shields.io/badge/ORCID-0009--0004--3627--6997-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0004-3627-6997)
[![Zenodo Master DOI](https://img.shields.io/badge/Zenodo_Master_DOI-10.5281%2Fzenodo.22804010-blue?logo=zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.22804010)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white&style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Research_Preprint-blue?style=flat-square)

> **"Deconstructing Riemann Zeros into Unitary Prime Oscillators and Real-Space Crystal Architectures"**  
> An open-science research framework connecting microscopic prime-phase spectroscopy, many-body quantum chaos, and operator gauge dynamics along the critical line Re(s) = 1/2 to the first-principles inverse design of 2D high-Tc superconducting parents.

---

![K-Protocol Master Architecture](00_k_protocol_master_architecture.png)

---

## Repository Structure & Research Roadmap

This repository is organized into four independent, sequential research tiers corresponding to each phase of the unified framework:

| Directory | Scope & Analytical Focus | Key Deliverables & Methodologies | Core Milestone |
| :--- | :--- | :--- | :--- |
| [**`01/`**](./01) | **Part I: Prime Phase Interference Spectroscopy**<br>Pairwise 2D destructive interference, Selberg resonance trenches, and Riemann-Siegel baseline calibration across 200 consecutive zeros. | • Full Theoretical Manuscript (`.pdf`)<br>• 2D interaction tensor survey (`k_protocol_master.py`)<br>• Selberg resonance trench sweep (`prime_resonance_radar.py`) | IR Potential Basin ($(p,q \le 7)$ captures 85.5% of zeros) |
| [**`02/`**](./02) | **Part II: Fock Coherence & Operator Gauge Stability**<br>Brody spectral rigidity, bipartite Fock-space entanglement phase transitions, and machine-precision Hermiticity rupture. | • Full Theoretical Manuscript (`.pdf`)<br>• GUE spacing & Coulomb barrier (`02_01_gue_level_repulsion.py`)<br>• Entanglement entropy transition (`02_02_fock_entanglement_transition.py`)<br>• Operator Hermiticity rupture (`02_07_reflection_gauge_hermiticity_rupture.py`) | +21.6% Entanglement surge; Exact Hermiticity iff $\sigma = 1/2$ |
| [**`03/`**](./03) | **Part III: Quantum Many-Body Rigidity & Bifurcation**<br>5-body Effective Field Theory (EFT) truncation proofs, resolvent singular wells, and complex pitchfork bifurcation dynamics. | • Full Theoretical Manuscript (`.pdf`)<br>• Real asymmetric resolvent tracking (`03_01_pipeline_08_resolvent_bifurcation.py`)<br>• Algebraic residue bound derivations | Lemma 1 ($k \le 5$ saturates 99.88%); Theorem 2 (Discriminant inversion) |
| [**`04/`**](./04) | **Part IV: Materials Inverse Design Engine**<br>Mapping 5-body EFT truncation to solid-state $MX_4$ plaquettes, apical steric gauge isolation, and automated DFT generation. | • Full Materials Science Manuscript (`.pdf`)<br>• Screening & QE automation (`04_01_k_protocol_miner.py`)<br>• 61-compound candidate database (`k_protocol_master_db.json`) | Blind re-discovery of $Sr_2CuO_2Cl_2$; Zero cross-plane dispersion |

---

## Core Scientific Highlights

1. **Microscopic Phase Interference (Part I):** Resolves the prime Dirichlet series modulus into an exact hyperbolic amplitude envelope $A_{pq} = 2/(pq)$, demonstrating that low-frequency primes govern destructive interference nodes.
2. **Operator Gauge Hermiticity (Part II):** Proves that the reflection gauge operator $A_{pq}(s) \equiv p^{-s}q^{-(1-s)}$ strictly preserves Hermiticity if and only if $\sigma = 1/2$, exhibiting catastrophic operator leakage off the critical boundary.
3. **Analytic 5-Body EFT Truncation (Part III):** Formulates Lemma 1, proving that interaction orders $k \le 5$ saturate $>99.87\%$ of multi-particle energy with an algebraic residue bound $R_{\ge 6} < 2.3 \times 10^{-7}$.
4. **Autonomous Materials Discovery (Part IV):** Enforces planar $C_4$ 5-body coordination and apical isolation ($c/a \ge 3.60, r_Y/r_X \ge 1.25$) under electroneutrality, autonomously identifying 61 parent compounds and independently validating the canonical benchmark $Sr_2CuO_2Cl_2$.

---

## Quick Start & Reproduction

Dependencies across all analytical pipelines require standard Python scientific computing libraries:

```bash
pip install numpy scipy mpmath matplotlib
