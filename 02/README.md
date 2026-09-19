# Part II: Quantum Spectral Rigidity, Fock-Space Entanglement, and Operator Gauge Rupture

[![ORCID](https://img.shields.io/badge/ORCID-0009--0004--3627--6997-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0004-3627-6997)
[![Zenodo Master DOI](https://img.shields.io/badge/Zenodo_Master_DOI-10.5281%2Fzenodo.22763956-blue?logo=zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.22763956)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white&style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Research_Preprint-blue?style=flat-square)

> **"Microscopic Quantum Many-Body Dynamics & Gauge Stability of Riemann Zeros"**  
> Demonstrating GUE level repulsion, Fock-space entanglement phase transitions, and machine-precision operator Hermiticity rupture along the critical boundary Re(s) = 1/2.

---

## Overview

This directory contains the official research manuscript and verification pipelines (`01`–`07`) for **Part II** of the unified K-Protocol framework.

Extending the pairwise 2D interference spectroscopy established in Part I, this work formulates the microscopic multi-particle quantum dynamics of the prime-phase lattice. By mapping prime oscillators into a Fock-space generating polynomial framework, we verify that critical zeros emerge as quantum coherent resonance nodes exhibiting strict Gaussian Unitary Ensemble (GUE) level repulsion, entanglement entropy surges, and an algebraic 5-body interaction cutoff. Furthermore, it establishes a rigorous proof that the fundamental reflection gauge operator preserves Hermiticity if and only if $\sigma = 1/2$.

* **Unified Master DOI:** [10.5281/zenodo.22763956](https://doi.org/10.5281/zenodo.22763956)
* **Parent Repository:** [k-protocol-riemann-zeros](https://github.com/CitizenKorea/k-protocol-riemann-zeros)

---

## Key Scientific Findings

### 1. Microscopic GUE Level Repulsion (`01_gue_level_repulsion.py`)
* The nearest-neighbor spacing distribution $P(s)$ of the prime interference matrix reconstructs the Dyson-Montgomery GUE Wigner surmise:
  $$P(s) \approx \frac{32}{\pi^2} s^2 \exp\left(-\frac{4}{\pi} s^2\right)$$
* Eliminates Poissonian clustering ($P(0) = 0$) and yields an empirical Brody parameter $\beta = 1.764 \pm 0.081$, establishing a logarithmic Coulomb barrier ($V_{eff} \approx -1.76 \ln s$) driven by prime phase anti-correlations.

### 2. Fock-Space Entanglement Phase Transition (`02_fock_entanglement_transition.py`)
* Decomposing the 100-prime generating polynomial into bipartitions of Fock subspaces reveals a sharp **+21.6% absolute surge in Von Neumann entanglement entropy** ($S_{Fock}$) precisely at exact zero crossings ($p = 2.14 \times 10^{-16}$).
* Demonstrates that non-trivial zeros represent macroscopic phase-locking transitions across microscopic oscillator states.

### 3. Algebraic N-Body Decoupling & 5-Body Cutoff (`03_nbody_algebraic_decoupling.py`)
* Multi-particle symmetric polynomial interactions satisfy an absolute algebraic bound:
  $$\vert{}S_{100}(t)\vert{} \le \prod_{j=1}^{100} \frac{1}{\sqrt{p_j}} = 1.4568 \times 10^{-110}$$
* Orders $k \le 5$ capture **99.8718% of total spectral energy**, confirming that higher-order multiparticle fluctuations ($k \ge 6$) decouple exponentially and justifying a 5-body Effective Field Theory (EFT) truncation.

### 4. Sub-Critical Saturation Breakdown (`04_off_critical_stress_test.py`)
* Evaluating saturation across $\sigma \in [0.20, 0.80]$ verifies that energy confinement is uniquely stable on the critical line $\sigma = 1/2$.
* Shifting off-axis ($\sigma < 1/2$) triggers a severe collapse in energy saturation (falling below 76.5% at $\sigma = 0.20$), indicating the structural failure of decoupled manifolds.

### 5. Macro Remainder Tail Decoupling (`05_euler_maclaurin_tail_test.py`)
* Evaluates the Euler-Maclaurin asymptotic remainder tail coupling, confirming that the macroscopic integral baseline decouples from the microscopic resonance lattice without introducing phase distortion.

### 6. Contour Integral Blowup (`06_carleman_contour_blowup.py`)
* Computes Littlewood-Jensen and Carleman-type boundary contour integrals, demonstrating an $L^2$ energy norm divergence whenever evaluation points are displaced into the sub-critical half-plane $\sigma < 1/2$.

### 7. Gauge Operator Hermiticity Rupture (`07_reflection_gauge_hermiticity_rupture.py`)
* Evaluates the reflection gauge operator $A_{pq}(s) \equiv p^{-s}q^{-(1-s)}$ across arbitrary complex coordinates $s = \sigma + it$.
* Proves that the non-Hermitian defect $\Gamma_{pq} = A_{pq}(s) - A_{qp}(s)^*$ vanishes to machine precision ($\Vert{}\Gamma\Vert{}_F = 5.159 \times 10^{-17}$) if and only if $\sigma = 1/2$, exhibiting immediate operator rupture off the critical axis.

---

## Directory Structure

```text
02/
├── Prime_Phase_Interference_Riemann_Zeros2v2.pdf   # Complete Part II theoretical manuscript
├── 01_gue_level_repulsion.py                   # Pipeline 01: GUE level repulsion & Brody parameter
├── 02_fock_entanglement_transition.py         # Pipeline 02: Fock-space Von Neumann entanglement entropy
├── 03_nbody_algebraic_decoupling.py            # Pipeline 03: 5-body generating polynomial energy saturation
├── 04_off_critical_stress_test.py              # Pipeline 04: Off-critical stability & saturation rupture
├── 05_euler_maclaurin_tail_test.py             # Pipeline 05: Macro Euler-Maclaurin remainder tail coupling
├── 06_carleman_contour_blowup.py               # Pipeline 06: Littlewood-Jensen contour integral divergence
├── 07_reflection_gauge_hermiticity_rupture.py  # Pipeline 07: Proof of Hermiticity rupture for sigma != 1/2
└── README.md                                   # Directory documentation
```

---

## Reproduction & Execution

All analytical scripts execute independently within the standard scientific Python ecosystem:

```bash
pip install numpy scipy mpmath matplotlib
```

### Reproducing GUE Spacing & Brody Distribution
```bash
python 01_gue_level_repulsion.py
```

### Reproducing Fock-Space Entanglement Surge
```bash
python 02_fock_entanglement_transition.py
```

### Reproducing Reflection Gauge Hermiticity Proof
```bash
python 07_reflection_gauge_hermiticity_rupture.py
```

---

## Citation

```bibtex
@misc{k_protocol_master_suite_2026,
  author       = {{A Citizen of the Republic of Korea}},
  title        = {{K-Protocol Unified Research Suite: From Analytic Number Theory to 2D High-Tc Superconducting Inverse Design (Parts I--IV)}},
  howpublished = {Zenodo},
  year         = {2026},
  doi          = {10.5281/zenodo.22763956},
  url          = {[https://doi.org/10.5281/zenodo.22763956](https://doi.org/10.5281/zenodo.22763956)}
}
```
