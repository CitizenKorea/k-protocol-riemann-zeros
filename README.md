# K-Protocol: Unified Operator Theory & Superconductor Inverse Design Suite

[![ORCID](https://img.shields.io/badge/ORCID-0009--0004--3627--6997-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0004-3627-6997)
[![Zenodo Master DOI](https://img.shields.io/badge/Zenodo_Master_DOI-10.5281%2Fzenodo.22763956-blue?logo=zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.22763956)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white&style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Research_Preprint-blue?style=flat-square)

> **"Deconstructing Riemann Zeros into Unitary Prime Oscillators and Real-Space Crystal Architectures"**  
> An open-science research framework connecting microscopic prime-phase spectroscopy, operator self-adjointness along $\mathrm{Re}(s) = 1/2$, and Computer-Assisted Proofs (CAP) of Phragmén-Lindelöf boundary ruptures to the first-principles inverse design of 2D high-Tc superconducting parents.

---

![K-Protocol Master Architecture](k_protocol_master_architecture.png)

---

## Repository Structure & Research Roadmap

This repository is organized into four sequential research modules corresponding to each phase of the framework:

| Directory | Scope & Analytical Focus | Key Deliverables & Methodologies | Core Milestone |
| :--- | :--- | :--- | :--- |
| [**`01/`**](./01) | **Part I: Prime Phase Interference Spectroscopy**<br>Pairwise 2D destructive interference, Selberg resonance trenches, and Riemann-Siegel baseline calibration across 200 consecutive zeros. | • Full Manuscript (`.pdf`)<br>• `01_prime_resonance_radar.py`<br>• `02_k_protocol_spectral_profiler.py`<br>• `03_k_protocol_master.py`<br>• `04_k_protocol_100th_zero_nbody.py` | IR Potential Basin ($(p,q \le 7)$ captures 85.5% of zeros) |
| [**`02/`**](./02) | **Part II: Fock Coherence & Operator Gauge Stability**<br>Brody spectral rigidity, bipartite Fock-space entanglement transitions, and machine-precision Hermiticity rupture. | • Full Manuscript (`.pdf`)<br>• `01_gue_level_repulsion.py`<br>• `02_fock_entanglement_transition.py`<br>• `03_nbody_algebraic_decoupling.py`<br>• `04_off_critical_stress_test.py`<br>• `05_euler_maclaurin_tail_test.py`<br>• `06_carleman_contour_blowup.py`<br>• `07_reflection_gauge_hermiticity_rupture.py` | +21.6% Entanglement surge; Exact Hermiticity iff $\sigma = 1/2$ |
| [**`03/`**](./03) | **Part III: Quantum Many-Body Rigidity, Operator Defects & Lindelöf Rupture**<br>5-body EFT truncation, complex pitchfork bifurcations, Cayley unitary defects, 35-digit ball CAP, and Phragmén-Lindelöf boundary contradictions. | • Manuscripts (Papers I & II)<br>• `01_pipeline_08_resolvent_bifurcation.py`<br>• `02_01_verify_k_protocol_rigor.py`<br>• `02_02_k_protocol_cayley_jensen_solver.py`<br>• `02_03_verify_uniform_lindelof_rupture.py`<br>• `02_04_verify_dirichlet_ball_arithmetic_unified.py`<br>• `02_04_protocol_cayley_jensen_unified.png` | Lemma 1 ($\alpha_{\min} \ge 0.8863$); Cayley unitary defect $\Vert{}\mathcal{U}^\dagger \mathcal{U} - I\Vert{}_F \equiv 0$; 1,563x Phragmén-Lindelöf uniform rupture |
| [**`04/`**](./04) | **Part IV: Materials Inverse Design Engine**<br>Mapping 5-body EFT truncation to solid-state $MX_4$ plaquettes, apical steric gauge isolation, and automated DFT generation. | • Full Materials Science Manuscript (`.pdf`)<br>• `01_k_protocol_miner.py`<br>• `k_protocol_master_db.json` (61 candidates) | Blind re-discovery of $Sr_2CuO_2Cl_2$; Zero cross-plane dispersion ($t_z \to 0$) |

---

## Core Scientific Highlights

1. **Microscopic Phase Interference (Part I):** Resolves the prime Dirichlet series modulus into an exact hyperbolic amplitude envelope $A_{pq} = 2/(pq)$, demonstrating that low-frequency primes govern destructive interference nodes.
2. **Operator Gauge Hermiticity (Part II):** Proves that the reflection gauge operator $A_{pq}(s) \equiv p^{-s}q^{-(1-s)}$ strictly preserves Hermiticity if and only if $\sigma = 1/2$, exhibiting catastrophic operator leakage off the critical boundary.
3. **Analytic 5-Body EFT Decoupling (Part III - Paper I):** Proves Lemma 1 via Cauchy saddle-point bounds, establishing an analytic decay lower bound $\alpha_{\min} \ge \ln 4 - 1/2 \approx 0.8863 > 0$ and bounding infinite tail fluctuations ($R_{\ge 6} < 2.3 \times 10^{-7}$). Proves Theorem 2, showing that off-critical coordinate displacements force pairwise discriminants to invert ($\mathcal{D}_{pq} < 0$), driving irreversible complex pitchfork bifurcations.
4. **Cayley Defect & Phragmén-Lindelöf Boundary Contradiction (Part III - Paper II):** 
   * **Monodromy Invariance CAP:** Regularizes $A(s)$ via second Carleman-Fredholm determinants $\det_2(I - A(s)) = \zeta(s)^{-1} \exp(P(s))$. Using 35-digit ball arithmetic, proves branch-cut annihilation within an enclosed ball radius of $\pm 3.52 \times 10^{-30}$.
   * **Cayley Operator Self-Adjointness:** Demonstrates that the Cayley transform $\mathcal{U}(s) = (\mathcal{H} - iI)(\mathcal{H} + iI)^{-1}$ satisfies exact unitarity ($\Vert{}\mathcal{U}^\dagger \mathcal{U} - I\Vert{}_F = 2.82 \times 10^{-15}$) strictly at $\sigma = 0.50$, while off-critical displacements eject eigenvalues from the unit disk.
   * **Uniform Growth Rupture:** Composite Simpson quadrature ($8,001$ nodes) demonstrates that $L^2$ boundary energy breaches the Phragmén-Lindelöf convexity ceiling by **1,563.1x**, with Dini's theorem guaranteeing uniform divergence across compact sub-critical intervals.
5. **Autonomous Materials Discovery (Part IV):** Enforces planar $C_4$ 5-body coordination and apical isolation ($c/a \ge 3.60, r_Y/r_X \ge 1.25$) under electroneutrality, autonomously identifying 61 parent compounds and independently validating the canonical benchmark $Sr_2CuO_2Cl_2$.

---

## Quick Start & Reproduction

Dependencies across all analytical pipelines require standard Python scientific computing libraries:

```bash
pip install numpy scipy mpmath matplotlib
```

### Reproducing Part I: Microscopic Interference
```bash
cd 01
python 03_k_protocol_master.py
```

### Reproducing Part II: Operator Gauge Rupture Proof
```bash
cd 02
python 07_reflection_gauge_hermiticity_rupture.py
```

### Reproducing Part III: Comprehensive Verification Suite & Solvers
```bash
cd 03

# 1. Run 4-Tier Independent Proof Audit (Theorems 1-2, Lemma 1, Fock Coherence)
python 02_01_verify_k_protocol_rigor.py

# 2. Run Cayley Unitary Defect & Spectral Escape Solver
python 02_02_k_protocol_cayley_jensen_solver.py

# 3. Audit Simpson Quadrature vs. Phragmén-Lindelöf Ceiling (Dini Uniformity)
python 02_03_verify_uniform_lindelof_rupture.py

# 4. Execute 35-Digit Complex Ball Arithmetic CAP Engine
python 02_04_verify_dirichlet_ball_arithmetic_unified.py
```

### Reproducing Part IV: 2D Materials Screening
```bash
cd 04
python 01_k_protocol_miner.py --database k_protocol_master_db.json --generate-qe
```

---

## How to Cite

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
