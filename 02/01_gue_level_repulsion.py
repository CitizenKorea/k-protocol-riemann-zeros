"""
========================================================================================
K-PROTOCOL: DYNAMICAL GUE LEVEL REPULSION & COULOMB BARRIER
Script: 01_gue_level_repulsion.py
Target: First 200 Consecutive Riemann Zeros x 1,000 Primes (499,500 Pairs)
Physical Derivation: Montgomery-Odlyzko GUE Spectral Rigidity via Prime Dephasing
Author: A Citizen of the Republic of Korea (estake@naver.com)
Date: September 2026
License: Creative Commons Attribution 4.0 International (CC BY 4.0)
========================================================================================
"""

import os
import time
import matplotlib.pyplot as plt
import mpmath
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.special import gamma

# =========================================================================
# 1. High-Precision Precision Configuration & Terminal Banner
# =========================================================================
mpmath.mp.dps = 25
CONSOLE_WIDTH = 90

print("=" * CONSOLE_WIDTH)
print("  K-PROTOCOL: DYNAMICAL GUE LEVEL REPULSION & COULOMB BARRIER")
print("  Physical Derivation of Spectral Rigidity from 2D Prime Phase Interference")
print("=" * CONSOLE_WIDTH)


# =========================================================================
# 2. Optimized Boolean Sieve for Generating Prime Oscillators
# =========================================================================
def generate_prime_ensemble(n: int = 1000) -> np.ndarray:
    """Generates the first n prime numbers using an optimized boolean sieve."""
    primes = []
    sieve_size = max(15000, n * 15)
    sieve = np.ones(sieve_size, dtype=bool)
    for p in range(2, len(sieve)):
        if sieve[p]:
            primes.append(p)
            if len(primes) == n:
                break
            sieve[p * p :: p] = False
    return np.array(primes, dtype=np.float64)


# =========================================================================
# 3. Benchmark Riemann Zero Importer (Cache-First, mpmath Fallback)
# =========================================================================
def acquire_riemann_zeros(num_zeros: int = 200) -> np.ndarray:
    """Acquires high-precision Riemann zeros from cache dat files or evaluates via mpmath."""
    cache_files = ["zeros_5000.dat", "zeros_26000.dat"]
    for dat_file in cache_files:
        if os.path.exists(dat_file):
            try:
                t_vals = []
                with open(dat_file, "r") as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith("#"):
                            t_vals.append(float(line.split()[-1]))
                            if len(t_vals) == num_zeros:
                                break
                if len(t_vals) == num_zeros:
                    print(f"  [Cache] Successfully loaded {num_zeros} benchmark zeros from '{dat_file}'.")
                    return np.array(t_vals, dtype=np.float64)
            except Exception:
                pass

    print(f"  [Compute] Evaluating first {num_zeros} non-trivial zeros via mpmath.zetazero...")
    t_start = time.perf_counter()
    t_vals = [float(mpmath.zetazero(i).imag) for i in range(1, num_zeros + 1)]
    print(f"            Computed {num_zeros} zeros in {time.perf_counter() - t_start:.2f} seconds.")
    return np.array(t_vals, dtype=np.float64)


# =========================================================================
# 4. Spectral Unfolding & Statistical Distribution Functions
# =========================================================================
def riemann_siegel_smooth_counting(t: np.ndarray) -> np.ndarray:
    """Evaluates the smooth Riemann-Siegel counting function N_0(t) for spectral unfolding."""
    return (t / (2.0 * np.pi)) * np.log(t / (2.0 * np.pi * np.e)) + (7.0 / 8.0)


def brody_pdf(s: np.ndarray, beta: float) -> np.ndarray:
    """Brody interpolation PDF bridging Poisson (beta=0), GOE (beta=1), and GUE (beta=2)."""
    b = (gamma((beta + 2.0) / (beta + 1.0))) ** (beta + 1.0)
    a = (beta + 1.0) * b
    return a * (s ** beta) * np.exp(-b * (s ** (beta + 1.0)))


# =========================================================================
# 5. Core Execution Engine
# =========================================================================
def run_pipeline(
    num_zeros: int = 200,
    num_primes: int = 1000,
    output_csv: str = "01_gue_level_repulsion_results.csv",
    output_png: str = "01_gue_level_repulsion_analysis.png",
):
    t_start_global = time.perf_counter()

    # Step 1: Prime Ensemble & Pairwise Coupling Vectorization
    print(f"\n[Phase 1] Constructing 2D Pairwise Coupling Lattice (N={num_primes:,} primes)...")
    primes = generate_prime_ensemble(num_primes)
    log_p = np.log(primes)
    inv_p = 1.0 / primes
    p_2_baseline = np.sum(inv_p ** 2)

    P = primes[:, None]
    Q = primes[None, :]
    mask = np.triu_indices(num_primes, k=1)
    p_vec = P[mask[0], 0]
    q_vec = Q[0, mask[1]]
    amp_vec = 2.0 / (p_vec * q_vec)
    log_ratio_vec = np.log(p_vec / q_vec)
    total_pairs = len(p_vec)
    print(f"          Unique pairwise interaction channels: {total_pairs:,}")

    # Step 2: Acquire Critical Zeros & Spectral Unfolding
    print(f"\n[Phase 2] Acquiring {num_zeros} zeros and executing spectral unfolding...")
    zeros = acquire_riemann_zeros(num_zeros)
    unfolded_zeros = riemann_siegel_smooth_counting(zeros)
    s_spacings = np.diff(unfolded_zeros)  # Normalized spacing: mean should be ~ 1.0
    raw_spacings = np.diff(zeros)

    print(f"          Range: t_1 = {zeros[0]:.6f} --> t_{num_zeros} = {zeros[-1]:.6f}")
    print(f"          Normalized Spacing Mean (s) : {np.mean(s_spacings):.6f} (Target: 1.000000)")
    print(f"          Normalized Spacing Std (s)  : {np.std(s_spacings):.6f}")

    # Step 3: Microscopic Leader Hegemony & Dephasing Compression Tracking
    print(f"\n[Phase 3] Profiling dominant destructive pairs and dephasing scales across zeros...")
    zero_records = []
    for idx, t_k in enumerate(zeros):
        phases = np.cos(t_k * log_ratio_vec)
        impacts = amp_vec * phases
        best_pos = np.argmin(impacts)
        p_lead = int(p_vec[best_pos])
        q_lead = int(q_vec[best_pos])
        cycle = np.pi / np.abs(np.log(q_lead / p_lead))

        zero_records.append({
            "zero_idx": idx + 1,
            "t_k": t_k,
            "p_lead": p_lead,
            "q_lead": q_lead,
            "pair_str": f"({p_lead}, {q_lead})",
            "impact_score": impacts[best_pos],
            "phase_cos": phases[best_pos],
            "dephasing_cycle": cycle,
        })
    df_zeros = pd.DataFrame(zero_records)

    switches = (df_zeros["pair_str"] != df_zeros["pair_str"].shift(1)).sum() - 1
    hegemony_rate = (switches / (num_zeros - 1)) * 100.0
    print(f"          Hegemony switches detected: {switches} / {num_zeros - 1} ({hegemony_rate:.2f}%)")

    # Step 4: High-Resolution Scan of Inter-Zero Lattice Phase Barriers
    print(f"\n[Phase 4] Computing inter-zero lattice energy barrier Delta Phi and restored stiffness...")
    barrier_heights = []
    stiffness_values = []

    for k in range(num_zeros - 1):
        t_a = zeros[k]
        t_b = zeros[k + 1]

        # 40-step trajectory evaluation across the interval [t_a, t_b]
        sub_t = np.linspace(t_a, t_b, 41)
        sub_phases = np.exp(-1j * np.outer(sub_t, log_p))
        dirichlet_sum = sub_phases @ inv_p
        phi_curve = np.abs(dirichlet_sum) ** 2 - p_2_baseline

        barrier = np.max(phi_curve) - 0.5 * (phi_curve[0] + phi_curve[-1])
        barrier_heights.append(barrier)

        # Numerical curvature (restoring spring constant) K = d^2 Phi / dt^2
        eps = 1e-4
        t_pts = np.array([t_a - eps, t_a, t_a + eps])
        d_pts = np.abs(np.exp(-1j * np.outer(t_pts, log_p)) @ inv_p) ** 2 - p_2_baseline
        curvature = (d_pts[2] - 2.0 * d_pts[1] + d_pts[0]) / (eps ** 2)
        stiffness_values.append(curvature)

    barrier_heights = np.array(barrier_heights)
    stiffness_values = np.array(stiffness_values)

    df_intervals = pd.DataFrame({
        "interval_idx": np.arange(1, num_zeros),
        "t_k": zeros[:-1],
        "delta_t": raw_spacings,
        "s_spacing": s_spacings,
        "barrier_height": barrier_heights,
        "lattice_stiffness": stiffness_values,
        "lead_dephasing": df_zeros["dephasing_cycle"].values[:-1],
        "lead_pair": df_zeros["pair_str"].values[:-1],
    })
    df_intervals.to_csv(output_csv, index=False, encoding="utf-8-sig")
    print(f"          Interval dataset exported to: {output_csv}")

    # Step 5: Brody Parameter Estimation & Repulsion Rigidity Fit
    hist_counts, bin_edges = np.histogram(s_spacings, bins=18, density=True)
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

    popt, _ = curve_fit(brody_pdf, bin_centers, hist_counts, p0=[1.8], bounds=(0.0, 3.5))
    fitted_beta = popt[0]

    # Step 6: Formatted Academic Console Output
    print("\n" + "=" * CONSOLE_WIDTH)
    print("  TABLE 1: Quantitative GUE Spectral Rigidity & Dynamical Repulsion Metrics")
    print("=" * CONSOLE_WIDTH)
    print(f"  {'Physical / Statistical Metric':<40} | {'Empirical Value':<18} | {'Theoretical Reference'}")
    print("  " + "-" * (CONSOLE_WIDTH - 4))
    print(f"  {'Fitted Brody Parameter (beta)':<40} | {fitted_beta:<18.4f} | beta = 2.0000 (Pure GUE Limit)")
    print(f"  {'Coalescence Probability P(s -> 0)':<40} | {hist_counts[0]:<18.4f} | 0.0000 (Strict Level Repulsion)")
    print(f"  {'Leader Hegemony Switching Rate':<40} | {hegemony_rate:<17.2f}% | High-Frequency Mode Actuation")
    print(f"  {'Mean Restoring Lattice Stiffness (K)':<40} | {np.mean(stiffness_values):<18.4f} | Confining Energy Well (K > 0)")
    print(f"  {'Mean Inter-Zero Phase Barrier (Delta Phi)':<40} | {np.mean(barrier_heights):<18.4f} | Anti-Phase Coalescence Shield")
    print("-" * CONSOLE_WIDTH)

    top_close = df_intervals.sort_values("s_spacing").head(5)
    print("\n" + "=" * CONSOLE_WIDTH)
    print("  TABLE 2: Top 5 Near-Collision Zero Intervals & Microscopic Shielding Dynamics")
    print("=" * CONSOLE_WIDTH)
    print(f"  {'Rank':<5} | {'Zero t_k':<12} | {'Spacing (s)':<12} | {'Barrier Delta Phi':<18} | {'Leader Pair':<14} | {'Dephasing Scale'}")
    print("  " + "-" * (CONSOLE_WIDTH - 4))
    for rank_i, (_, r) in enumerate(top_close.iterrows(), start=1):
        print(f"  #{rank_i:<4} | {r.t_k:<12.4f} | {r.s_spacing:<12.4f} | {r.barrier_height:<18.6f} | {r.lead_pair:<14} | {r.lead_dephasing:<12.4f}")
    print("=" * CONSOLE_WIDTH)

    # Step 7: Publication-Grade 4-Panel Visualization
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))

    # Panel 1: Spacing Distribution P(s) vs GUE vs Poisson
    s_dense = np.linspace(0.01, 3.2, 300)
    p_poisson = np.exp(-s_dense)
    p_gue = (32.0 / (np.pi ** 2)) * (s_dense ** 2) * np.exp(-(4.0 / np.pi) * (s_dense ** 2))
    p_brody = brody_pdf(s_dense, fitted_beta)

    axes[0, 0].hist(s_spacings, bins=18, density=True, color="#2b5c8f", alpha=0.7, edgecolor="white", label="Empirical Spacings (200 Zeros)")
    axes[0, 0].plot(s_dense, p_gue, "r-", lw=2.2, label=r"GUE Wigner Surmise ($\beta=2$)")
    axes[0, 0].plot(s_dense, p_poisson, "k--", lw=1.5, alpha=0.7, label=r"Poisson Random ($\beta=0$)")
    axes[0, 0].plot(s_dense, p_brody, "g-.", lw=2.0, label=rf"Fitted Brody ($\beta={fitted_beta:.2f}$)")
    axes[0, 0].set_title(r"Nearest-Neighbor Spacing Distribution $P(s)$ (Level Repulsion)", fontsize=12, fontweight="bold")
    axes[0, 0].set_xlabel("Normalized Spacing (s)")
    axes[0, 0].set_ylabel("Probability Density P(s)")
    axes[0, 0].legend(frameon=True, loc="upper right")
    axes[0, 0].grid(True, linestyle="--", alpha=0.5)

    # Panel 2: Effective Coulomb Logarithmic Barrier V_eff(s) = -ln P(s)
    valid_mask = hist_counts > 0
    s_valid = bin_centers[valid_mask]
    v_eff_emp = -np.log(hist_counts[valid_mask])
    v_eff_gue = -np.log(np.maximum(1e-6, (32.0 / (np.pi ** 2)) * (s_dense ** 2) * np.exp(-(4.0 / np.pi) * (s_dense ** 2))))

    axes[0, 1].scatter(s_valid, v_eff_emp, color="#c0392b", s=45, zorder=5, label=r"Empirical $V_{\mathrm{eff}}(s) = -\ln P(s)$")
    axes[0, 1].plot(s_dense, v_eff_gue, "r-", lw=2.0, label=r"GUE Coulomb Well $\sim -2\ln(s)$")
    axes[0, 1].plot(s_dense, -2.0 * np.log(s_dense), "b:", lw=1.5, label=r"Pure Logarithmic Barrier $-2\ln s$")
    axes[0, 1].set_title(r"Effective Repulsion Potential $V_{\mathrm{eff}}(s)$ as $s \to 0$", fontsize=12, fontweight="bold")
    axes[0, 1].set_xlabel("Normalized Spacing (s)")
    axes[0, 1].set_ylabel(r"Potential Energy $V_{\mathrm{eff}}(s)$")
    axes[0, 1].set_ylim(-0.5, 5.0)
    axes[0, 1].legend(frameon=True, loc="upper right")
    axes[0, 1].grid(True, linestyle="--", alpha=0.5)

    # Panel 3: Dephasing Scale Compression & Mean Spacing Tracking
    mean_spacing_theory = 2.0 * np.pi / np.log(zeros[:-1] / (2.0 * np.pi))
    axes[1, 0].scatter(zeros[:-1], raw_spacings, color="#7f8c8d", alpha=0.5, s=16, label=r"Empirical $\Delta t_k$")
    axes[1, 0].plot(zeros[:-1], mean_spacing_theory, color="#e74c3c", lw=2.0, label=r"Asymptotic Mean $\langle\Delta t\rangle = \frac{2\pi}{\ln(t/2\pi)}$")
    axes[1, 0].plot(zeros[:-1], df_zeros["dephasing_cycle"].values[:-1], color="#2980b9", lw=1.2, alpha=0.7, label=r"Leader Dephasing $\Delta t_{\mathrm{cycle}}(p, q)$")
    axes[1, 0].set_title("Dephasing Scale Compression vs. Mean Zero Spacing", fontsize=12, fontweight="bold")
    axes[1, 0].set_xlabel("Riemann Zero Height (t)")
    axes[1, 0].set_ylabel("Spectral Spacing / Dephasing Scale")
    axes[1, 0].legend(frameon=True, loc="upper right")
    axes[1, 0].grid(True, linestyle="--", alpha=0.5)

    # Panel 4: Lattice Phase Barrier vs. Normalized Spacing
    scatter = axes[1, 1].scatter(
        df_intervals["s_spacing"],
        df_intervals["barrier_height"],
        c=df_intervals["t_k"],
        cmap="viridis",
        alpha=0.8,
        s=32,
    )
    cbar = fig.colorbar(scatter, ax=axes[1, 1])
    cbar.set_label("Zero Coordinate (t_k)", fontsize=10)
    axes[1, 1].set_title("Lattice Phase Barrier Height vs. Zero Spacing", fontsize=12, fontweight="bold")
    axes[1, 1].set_xlabel("Normalized Spacing (s)")
    axes[1, 1].set_ylabel(r"Lattice Phase Barrier $\Delta\Phi$")
    axes[1, 1].grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.savefig(output_png, dpi=300)
    total_time = time.perf_counter() - t_start_global
    print(f"\n[Output] High-resolution diagnostic plot exported: {output_png}")
    print(f"[Execution] Script 01 completed successfully in {total_time:.2f} seconds.")
    plt.show()


if __name__ == "__main__":
    run_pipeline(
        num_zeros=200,
        num_primes=1000,
        output_csv="01_gue_level_repulsion_results.csv",
        output_png="01_gue_level_repulsion_analysis.png",
    )