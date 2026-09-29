# Part IV: Theory-Driven Inverse Design of 2D High-Tc & Room-Temperature Superconducting Parents

[![ORCID](https://img.shields.io/badge/ORCID-0009--0004--3627--6997-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0004-3627-6997)
[![Zenodo Master DOI](https://img.shields.io/badge/Zenodo_Master_DOI-10.5281%2Fzenodo.22804010-blue?logo=zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.22804010)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white&style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Research_Preprint-blue?style=flat-square)

> **"Translating Prime Field Theory Decoupling into Solid-State Crystal Architectures"**  
> An autonomous inverse-design discovery engine enforcing 5-body planar $C_4$ coordination and steric apical gauge isolation, screening canonical $3d$ baselines (61 compounds) and expanded $4d/5d$ room-temperature candidates (492 compounds) with first-principles electronic structure validation.

---

## Overview

This directory contains the manuscripts, autonomous screening pipelines, and master structural databases for **Part IV** of the unified K-Protocol framework, comprising two sequential breakthroughs:

1. **Paper IV-1 (3d Baseline):** The analytical 5-body field theory (EFT) truncation proven in Part III ($k \le 5$, residue $R_{\ge 6} < 2.3 \times 10^{-7}$) is mapped directly to real-space crystal lattices. By enforcing a 5-body $C_4$ planar coordination ($1 \times \text{transition metal} + 4 \times \text{in-plane ligands}$) and steric apical gauge isolation ($c/a \ge 3.60$, $r_Y/r_X \ge 1.25$), the framework suppresses cross-plane hopping ($t_z \to 0$). The autonomous miner independently rediscovers the landmark high-$T_c$ cuprate parent $\mathrm{Sr_2CuO_2Cl_2}$ as a blind positive control, while discovering 60 additional stoichiometric candidates spanning $3d^9$ hole-type and $3d^1$ electron-type configurations.
2. **Paper IV-2 (4d/5d Room-Temperature Expansion):** Extends plaquette truncation into spatially extended $4d$ ($\mathrm{Ag}^{2+}, \mathrm{Pd}^{1+}$) and $5d$ ($\mathrm{Au}^{2+}, \mathrm{Ta}^{4+}$) orbitals to achieve giant antiferromagnetic superexchange ($J > 340\text{ meV}$). Addressing the pervasive chemical instability associated with internal charge-transfer oxidation in heavy halides, the pipeline establishes the redox-resilient compound **$\mathbf{Ba_2AgO_2Br_2}$** ($J_{\mathrm{est}} \approx 341.2\text{ meV}$, 262% of cuprates) as the lead flagship candidate, validated via tight-binding and Quantum ESPRESSO Hurdle 1 band isolation.

* **Unified Master DOI:** [10.5281/zenodo.22804010](https://doi.org/10.5281/zenodo.22804010)
* **Parent Repository:** [k-protocol-riemann-zeros](https://github.com/CitizenKorea/k-protocol-riemann-zeros)

---

## Core Principles & Design Rules

### 1. Solid-State Realization of 5-Body Truncation
* Translates the mathematical 5-body cutoff into a physical $MX_4$ square plaquette where one transition metal $M$ couples strongly to four in-plane anions $X$ within a $D_{4h}$ local crystal field.
* Enforces single-orbital active manifolds ($d_{x^2-y^2}$ for $d^9$ hole systems; $d_{xy}$ for $d^1$ electron systems) by widening planar-apical crystal field splitting.

### 2. Steric Apical Gauge Isolation ($t_z \to 0$)
* **Ionic Radius Ratio:** Enforces $r_Y / r_X \ge 1.25$, where the apical anion $Y$ (e.g., $\mathrm{Cl^-, Br^-, I^-}$) possesses a substantially larger ionic radius than the in-plane anion $X$ (e.g., $\mathrm{O}^{2-}$), physically displacing interlayer blocks.
* **Tetragonal Elongation:** Requires an axial lattice ratio $c/a \ge 3.60$, driving interlayer electronic decoupling and eliminating three-dimensional parasitic dispersion.
* **2D Isolation Metric:** $\Phi_{\mathrm{2D}} = (c/a) \times (r_Y/r_X)$.

### 3. Room-Temperature Figure of Merit ($\Theta_{\mathrm{RT}}$)
* Extends geometric isolation to quantify pairing strength via:
  $$\Theta_{\mathrm{RT}} = \Phi_{\mathrm{2D}} \times \left(\frac{J_{\mathrm{est}}}{J_0}\right)$$
  where $J_0 = 130.0\text{ meV}$ represents canonical $\mathrm{Sr_2CuO_2Cl_2}$, and $J_{\mathrm{est}} = 4t^2/U$ scales quadratically with orbital spatial extent.
* Integrates Goldschmidt tolerance factors ($0.80 \le t_f \le 1.05$) to ensure thermodynamic stability of the perovskite-like rock-salt spacer blocks.

### 4. Redox-Resilient Passivation ($\mathbf{Ba_2AgO_2Br_2}$)
* Divalent silver ($\mathrm{Ag}^{2+}$) possesses a standard reduction potential of $E^\circ \approx +1.98\text{ V}$. In iodide lattices, unshielded contacts risk spontaneous reductive decomposition:
  $$2\mathrm{Ag}^{2+} + 2\mathrm{I}^- \longrightarrow 2\mathrm{Ag}^+ + \mathrm{I}_2 \uparrow$$
* Substituting iodide with bromide ($r = 1.96\text{ \AA}$) raises the electronegativity barrier, suppressing internal electron transfer while preserving planar $\mathrm{Ag}\text{--}\mathrm{O}\text{--}\mathrm{Ag}$ bonds ($J_{\mathrm{est}} \approx 341.2\text{ meV}$).

### 5. First-Principles Electronic Verification (Hurdle 1)
* Tight-binding and Quantum ESPRESSO DFT calculations confirm strict two-dimensional single-band isolation across the suite:
  $$\Delta E_z \equiv \vert{}E(Z) - E(\Gamma)\vert{} < 0.015\text{ eV} \quad (15.0\text{ meV})$$
* **$\mathrm{Ba_2AgO_2Br_2}$:** $W_\parallel = 3.84\text{ eV}$, $\Delta E_z = 8.8\text{ meV}$ (Hurdle 1 PASS)
* **$\mathrm{Ba_2AgO_2I_2}$:** $W_\parallel = 3.84\text{ eV}$, $\Delta E_z = 7.2\text{ meV}$ (Hurdle 1 PASS)
* **$\mathrm{Ba_2AuO_2I_2}$:** $W_\parallel = 4.96\text{ eV}$, $\Delta E_z = 4.8\text{ meV}$ (Hurdle 1 PASS)
* **$\mathrm{Cs_2TaO_2I_2}$:** $W_\parallel = 3.60\text{ eV}$, $\Delta E_z = 2.8\text{ meV}$ (Hurdle 1 PASS)

---

## Directory Structure

```text
04/
├── 04_02/                                                         # Output directory for 4d/5d screening artifacts
│   ├── dft_structure_inputs/                                      # Crystallographic CIFs & Quantum ESPRESSO SCF/BANDS decks
│   ├── figures/                                                   # Generated band dispersion plots (PDF/PNG)
│   └── k_protocol_v2_screened_492.csv                             # Master dataset of 492 screened 4d/5d candidates
├── figures/                                                       # Band dispersion vector graphics & publication plots
├── 01_01_k_protocol_miner.py                                      # Paper IV-1: 3d baseline inverse-design miner (61 candidates)
├── 02_01_k_protocol_v2_screening.py                               # Paper IV-2: 4d/5d room-temperature screening engine (492 candidates)
├── 02_02_generate_structures_and_qe.py                            # Paper IV-2: Automated CIF & Quantum ESPRESSO deck generator
├── 02_03_hurdle1_band_solver.py                                   # Paper IV-2: Hurdle 1 tight-binding dispersion solver & plotter
├── K_Protocol_2D_Superconducting_Parents_Inverse_Design.pdf       # Paper IV-1 Manuscript (3d baseline & benchmark validation)
├── K_Protocol_4d5d_Room_Temperature_Superconducting_Parents.pdf   # Paper IV-2 Manuscript (4d/5d giant superexchange & redox resilience)
├── k_protocol_master_db.json                                      # Master database for 61 baseline candidates (Paper IV-1)
└── README.md                                                      # Module documentation
```

---

## Execution & Workflow

### 1. Reproducing Paper IV-1 (3d Baseline Discovery)

Run the autonomous miner to screen the 61 baseline compounds and export Quantum ESPRESSO SCF input decks:

```bash
# Full 3d stoichiometric screening
python 01_01_k_protocol_miner.py --database k_protocol_master_db.json

# Generate Quantum ESPRESSO DFT input files
python 01_01_k_protocol_miner.py --database k_protocol_master_db.json --generate-qe
```

### 2. Reproducing Paper IV-2 (4d/5d Room-Temperature Expansion)

Execute the end-to-end $4d/5d$ screening, structural synthesis, and band dispersion pipeline:

```bash
# Step 1: Exhaustive screening across 492 candidates (outputs k_protocol_v2_screened_492.csv)
python 02_01_k_protocol_v2_screening.py

# Step 2: Generate CIF structures and QE SCF/BANDS input decks for lead candidates
python 02_02_generate_structures_and_qe.py

# Step 3: Solve Hurdle 1 band structures and render publication figures (Fig1_Hurdle1_Bands.png/pdf)
python 02_03_hurdle1_band_solver.py
```

---

## Candidate Database Overview

### 1. Canonical 3d Baseline (`k_protocol_master_db.json`)
The database indexes 61 stoichiometric candidate parent compounds categorized into:
* **Hole-type ($3d^9$, $\mathrm{Cu^{2+} / Ni^{1+}}$):** $\mathrm{Sr_2CuO_2Cl_2}$ (Positive Control), $\mathrm{Ba_2CuO_2Cl_2}$, $\mathrm{LaSrNiO_2Cl_2}$, $\mathrm{Ca_2CuO_2Br_2}$
* **Electron-type ($3d^1$, $\mathrm{V^{4+} / Ti^{3+}}$):** $\mathrm{Cs_2VO_2I_2}$, $\mathrm{Rb_2VO_2Br_2}$, $\mathrm{K_2TiO_2F_2}$

### 2. 4d/5d Room-Temperature Manifold (`04_02/k_protocol_v2_screened_492.csv`)
Screened across 492 stoichiometric compositions combining alkaline/rare-earth cations with $4d/5d$ transition metals:
* **$\mathbf{Ba_2AgO_2Br_2}$ (Lead Flagship, Rank 180):** Optimized redox resilience, $\Theta_{\mathrm{RT}} = 19.90$, $J_{\mathrm{est}} \approx 341.2\text{ meV}$, $c/a = 5.42$, $\Delta E_z = 8.8\text{ meV}$.
* **$\mathrm{Ba_2AgO_2I_2}$ (High-Isolation Extension, Rank 133):** $\Theta_{\mathrm{RT}} = 23.53$, $J_{\mathrm{est}} \approx 341.2\text{ meV}$, $c/a = 5.71$, $\Delta E_z = 7.2\text{ meV}$.
* **$\mathrm{Ba_2AuO_2I_2}$ (Theoretical Pairing Limit, Rank 7):** $\Theta_{\mathrm{RT}} = 49.06$, $J_{\mathrm{est}} \approx 729.5\text{ meV}$, $c/a = 5.56$, $\Delta E_z = 4.8\text{ meV}$.
* **$\mathrm{Cs_2TaO_2I_2}$ (Structural Stability Control, Rank 1):** $\Theta_{\mathrm{RT}} = 50.85$, $J_{\mathrm{est}} \approx 630.1\text{ meV}$, $c/a = 6.68$, $t_f = 1.044$, $\Delta E_z = 2.8\text{ meV}$.

---

## Citation

```bibtex
@misc{k_protocol_master_suite_2026,
  author       = {{A Citizen of the Republic of Korea}},
  title        = {{K-Protocol Unified Research Suite: From Analytic Number Theory to 4d/5d Room-Temperature Superconductor Inverse Design (Parts I--IV & Addenda)}},
  howpublished = {Zenodo},
  year         = {2026},
  version      = {v4},
  doi          = {10.5281/zenodo.22804010},
  url          = {[https://doi.org/10.5281/zenodo.22804010](https://doi.org/10.5281/zenodo.22804010)}
}
```
