import os
import sys
import numpy as np
import matplotlib.pyplot as plt

# ==============================================================================
# [K-PROTOCOL Paper 04-2] Hurdle 1 Band Structure & Dispersion Validator
# High-Symmetry Path: Gamma(0,0,0) -> X(pi,0,0) -> M(pi,pi,0) -> Gamma -> Z(0,0,pi)
# Output Directory: ./figures/ (Relative to execution directory)
# ==============================================================================

# Ensure portable relative subfolder creation
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "figures")
os.makedirs(OUTPUT_DIR, exist_ok=True)

PNG_OUTPUT_PATH = os.path.join(OUTPUT_DIR, "Fig1_Hurdle1_Bands.png")
PDF_OUTPUT_PATH = os.path.join(OUTPUT_DIR, "Fig1_Hurdle1_Bands.pdf")

# Model Hamiltonian Parameters (DFT Wannier Mapping)
# Lead Champion (Br2) + Extension (I2) + Au Limit + Ta Control
MODELS = {
    r"$\mathbf{Ba_2AgO_2Br_2}$ ($4d^9$, Lead)": {
        "name": "Ba2AgO2Br2",
        "t": 0.48, "tp": -0.12, "tz": 0.0022, "color": "#0055ff", "linestyle": "-"
    },
    r"$\mathbf{Ba_2AgO_2I_2}$ ($4d^9$, Ext)": {
        "name": "Ba2AgO2I2",
        "t": 0.48, "tp": -0.12, "tz": 0.0018, "color": "#17becf", "linestyle": "--"
    },
    r"$\mathbf{Ba_2AuO_2I_2}$ ($5d^9$, Limit)": {
        "name": "Ba2AuO2I2",
        "t": 0.62, "tp": -0.16, "tz": 0.0012, "color": "#d62728", "linestyle": "-"
    },
    r"$\mathbf{Cs_2TaO_2I_2}$ ($5d^1$, Control)": {
        "name": "Cs2TaO2I2",
        "t": 0.45, "tp": -0.08, "tz": 0.0007, "color": "#2ca02c", "linestyle": "-"
    }
}

# Generate 201 High-Symmetry k-points (50 intervals per segment)
N = 50
k_path = (
    [np.array([kx, 0.0, 0.0]) for kx in np.linspace(0, np.pi, N, endpoint=False)] +
    [np.array([np.pi, ky, 0.0]) for ky in np.linspace(0, np.pi, N, endpoint=False)] +
    [np.array([k, k, 0.0]) for k in np.linspace(np.pi, 0, N, endpoint=False)] +
    [np.array([0.0, 0.0, kz]) for kz in np.linspace(0, np.pi, N + 1)]
)
k_idx = np.arange(len(k_path))

def solve_and_plot():
    print("=" * 80)
    print(" [K-PROTOCOL Paper 04-2] Hurdle 1 Single-Band Dispersion Analysis (4 Candidates)")
    print(" Strict 2D Isolation Criterion: Delta_Ez < 15.0 meV")
    print("=" * 80)

    plt.rcParams["font.family"] = "DejaVu Sans"
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

    for label_tex, p in MODELS.items():
        energies = []
        for k in k_path:
            kx, ky, kz = k[0], k[1], k[2]
            eps = (
                - 2.0 * p["t"] * (np.cos(kx) + np.cos(ky))
                + 4.0 * p["tp"] * np.cos(kx) * np.cos(ky)
                - 2.0 * p["tz"] * np.cos(kz)
            )
            energies.append(eps)
            
        energies = np.array(energies)
        energies -= np.mean(energies)  # Aligned to half-filling chemical potential
        
        # Calculate Delta E_z along Gamma (0,0,0) -> Z (0,0,pi)
        delta_ez = np.abs(energies[-1] - energies[-N-1]) * 1000.0  # in meV
        w_in = 8.0 * p["t"]                                        # in-plane bandwidth in eV
        status = "PASS" if delta_ez < 15.0 else "FAIL"

        print(f" -> Candidate: {p['name']:<14} | W_in: {w_in:.2f} eV | Delta_Ez: {delta_ez:4.1f} meV | Status: [{status}]")

        # Double backslashes used to prevent SyntaxWarnings in Python 3.12+
        legend_entry = f"{label_tex} : $W_{{\\parallel}}$={w_in:.2f} eV, $\\Delta E_z$={delta_ez:.1f} meV"
        ax.plot(k_idx, energies, label=legend_entry, color=p["color"], 
                linestyle=p["linestyle"], linewidth=2.0)

    # Plot formatting
    nodes = [0, N, 2 * N, 3 * N, 4 * N]
    node_labels = [r"$\Gamma$", r"$X$", r"$M$", r"$\Gamma$", r"$Z$"]
    for n in nodes:
        ax.axvline(n, color="gray", linestyle="--", linewidth=0.8, alpha=0.7)

    ax.axhline(0.0, color="black", linestyle=":", linewidth=1.2, label=r"Fermi Level ($E_F$)")
    ax.set_xticks(nodes)
    ax.set_xticklabels(node_labels, fontsize=12, fontweight="bold")
    ax.set_ylabel("Energy (eV)", fontsize=11, fontweight="bold")
    ax.set_title("K-Protocol Paper 04-2: Hurdle 1 Strict 2D Single-Band Isolation (4 Candidates)", 
                 fontsize=12, fontweight="bold")
    ax.set_xlim(0, len(k_path) - 1)
    ax.set_ylim(-3.5, 3.5)
    ax.grid(True, linestyle="--", alpha=0.3)
    ax.legend(loc="upper right", fontsize=9, framealpha=0.95)

    plt.tight_layout()

    # Save both PNG (web/view) and PDF (publication vector graphic)
    plt.savefig(PNG_OUTPUT_PATH, dpi=600)
    plt.savefig(PDF_OUTPUT_PATH)
    plt.close(fig)

    print("-" * 80)
    print("[SUCCESS] Output files successfully generated:")
    print(f"  - PNG Figure : {os.path.relpath(PNG_OUTPUT_PATH, SCRIPT_DIR)}")
    print(f"  - PDF Vector : {os.path.relpath(PDF_OUTPUT_PATH, SCRIPT_DIR)}")
    print("=" * 80)

if __name__ == "__main__":
    solve_and_plot()