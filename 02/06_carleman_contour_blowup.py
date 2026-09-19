"""
========================================================================================
K-PROTOCOL: CARLEMAN-JENSEN CONTOUR INTEGRAL & BOUNDARY BLOWUP TEST
Script: 06_carleman_contour_blowup.py
Target: Benchmark Zero #1 (t_1 ~ 14.134725) Across Rectangular Contours [sigma_0, 1.5] x [12, 16]
Physical Derivation: Phase Boundary Kink at sigma = 1/2 & Sub-Critical L2 Energy Rupture
Author: A Citizen of the Republic of Korea (estake@naver.com)
Date: September 2026
License: Creative Commons Attribution 4.0 International (CC BY 4.0)
========================================================================================
"""

import time
import matplotlib.pyplot as plt
import mpmath
import numpy as np
import pandas as pd

# NumPy 1.x vs 2.x backward/forward compatibility for trapezoidal integration
integrate_trapezoid = getattr(np, "trapezoid", getattr(np, "trapz", None))
if integrate_trapezoid is None:
    from scipy.integrate import trapezoid as integrate_trapezoid

# =========================================================================
# 1. High-Precision Precision Configuration & Terminal Banner
# =========================================================================
mpmath.mp.dps = 25
CONSOLE_WIDTH = 92

print("=" * CONSOLE_WIDTH)
print("  K-PROTOCOL: CARLEMAN-JENSEN CONTOUR INTEGRAL & BOUNDARY BLOWUP TEST")
print("  Evaluating Contour Balance and Sub-Critical L2-Energy Rupture (sigma < 1/2)")
print("=" * CONSOLE_WIDTH)


# =========================================================================
# 2. Optimized Boolean Sieve for Generating Prime Ensemble (Up to 300 Primes)
# =========================================================================
def generate_prime_ensemble(n: int = 300) -> np.ndarray:
    """Generates the first n prime numbers using an optimized boolean sieve."""
    primes = []
    sieve_size = max(5000, n * 15)
    sieve = np.ones(sieve_size, dtype=bool)
    for p in range(2, len(sieve)):
        if sieve[p]:
            primes.append(p)
            if len(primes) == n:
                break
            sieve[p * p :: p] = False
    return np.array(primes, dtype=np.float64)


# =========================================================================
# 3. Littlewood-Jensen Contour Integral on Rectangle R = [sigma_0, sigma_1] x [T1, T2]
# =========================================================================
def evaluate_littlewood_contour(
    sigma_0: float,
    sigma_1: float = 1.5,
    t1: float = 12.0,
    t2: float = 16.0,
    n_pts: int = 250,
):
    """Evaluates the Littlewood-Jensen rectangular contour integral of zeta(s).
    
    Formula:
      2*pi * sum_{rho in R} (beta_rho - sigma_0)
        = int_{T1}^{T2} ln|zeta(sigma_0 + it)| dt
        - int_{T1}^{T2} ln|zeta(sigma_1 + it)| dt
        + int_{sigma_0}^{sigma_1} arg zeta(sigma + i T2) dsigma
        - int_{sigma_0}^{sigma_1} arg zeta(sigma + i T1) dsigma
    """
    # 1. Left boundary: s = sigma_0 + i*t
    t_vals = np.linspace(t1, t2, n_pts)
    dt = (t2 - t1) / (n_pts - 1)
    vals_left = [float(mpmath.log(abs(mpmath.zeta(mpmath.mpc(sigma_0, t))))) for t in t_vals]
    int_left = float(integrate_trapezoid(vals_left, dx=dt))

    # 2. Right boundary: s = sigma_1 + i*t (sigma_1 = 1.5 in absolute convergence)
    vals_right = [float(mpmath.log(abs(mpmath.zeta(mpmath.mpc(sigma_1, t))))) for t in t_vals]
    int_right = float(integrate_trapezoid(vals_right, dx=dt))

    # 3. Horizontal boundaries (top and bottom arguments)
    sig_vals = np.linspace(sigma_0, sigma_1, n_pts)
    dsig = (sigma_1 - sigma_0) / (n_pts - 1)
    vals_top = [float(mpmath.arg(mpmath.zeta(mpmath.mpc(s, t2)))) for s in sig_vals]
    int_top = float(integrate_trapezoid(vals_top, dx=dsig))

    vals_bottom = [float(mpmath.arg(mpmath.zeta(mpmath.mpc(s, t1)))) for s in sig_vals]
    int_bottom = float(integrate_trapezoid(vals_bottom, dx=dsig))

    # Littlewood contour evaluation: estimated sum(beta - sigma_0)
    contour_sum = (int_left - int_right + int_top - int_bottom) / (2.0 * np.pi)

    # Ground truth for Zero #1 (beta_1 = 0.50, gamma_1 = 14.134725)
    exact_sum = max(0.0, 0.50 - sigma_0)

    return {
        "sigma_0": sigma_0,
        "exact_sum": exact_sum,
        "contour_sum": contour_sum,
        "int_left": int_left,
        "int_right": int_right,
        "int_top": int_top,
        "int_bottom": int_bottom,
        "error": abs(contour_sum - exact_sum),
    }


# =========================================================================
# 4. Prime Network Left-Boundary L2 Energy Density
# =========================================================================
def evaluate_boundary_l2_energy(
    sigma_0: float,
    primes_arr: np.ndarray,
    t1: float = 12.0,
    t2: float = 16.0,
    n_pts: int = 150,
):
    """Computes empirical and theoretical L2 boundary energy <|P_X|^2> on s = sigma_0 + it.
    
    Theoretical Asymptotic Mean:
      lim_{T -> infty} 1/(2T) int_{-T}^T |P_X(sigma_0 + it)|^2 dt = prod_{p <= X} (1 + p^{-2*sigma_0})
    """
    t_vals = np.linspace(t1, t2, n_pts)
    dt = (t2 - t1) / (n_pts - 1)

    log_p = np.log(primes_arr)
    # Phase oscillator matrix: shape (n_pts, len(primes))
    phase_matrix = np.exp(-1j * np.outer(t_vals, log_p)) * (primes_arr ** -sigma_0)

    # Evaluate multi-particle product: P_X(s) = prod_{p} (1 + p^{-s})
    poly_vals = np.prod(1.0 + phase_matrix, axis=1)
    energy_l2_emp = float(integrate_trapezoid(np.abs(poly_vals) ** 2, dx=dt) / (t2 - t1))

    # Theoretical ergodic expectation value
    energy_l2_th = float(np.prod(1.0 + primes_arr ** (-2.0 * sigma_0)))

    return energy_l2_emp, energy_l2_th


# =========================================================================
# 5. Core Execution Pipeline
# =========================================================================
def run_pipeline(
    output_csv: str = "06_carleman_contour_results.csv",
    output_png: str = "06_carleman_contour_analysis.png",
):
    t_start_global = time.perf_counter()

    # Step 1: Initialize Prime Ensembles (N = 50, 100, 300)
    primes_all = generate_prime_ensemble(300)
    primes_50 = primes_all[:50]
    primes_100 = primes_all[:100]
    primes_300 = primes_all[:300]
    print(f"\n[Phase 1] Prime ensembles generated (50, 100, 300 primes; Max Prime = {primes_300[-1]:.0f})...")

    # Step 2: Target Contour Specifications around Zero #1
    t1, t2 = 12.0, 16.0
    sigma_1 = 1.5
    zero_1 = float(mpmath.zetazero(1).imag)
    print(f"[Phase 2] Target contour set: [sigma_0, {sigma_1}] x [{t1}, {t2}] enclosing Zero #1 (t = {zero_1:.6f})")

    # Step 3: Discrete Parameter Sweep Across sigma_0
    sigma_discrete = [0.80, 0.70, 0.60, 0.50, 0.45, 0.40, 0.30, 0.20]
    records = []

    print("\n[Phase 3] Computing Littlewood contour and L2 boundary energies across discrete sigma_0...")
    for s0 in sigma_discrete:
        cw_res = evaluate_littlewood_contour(s0, sigma_1=sigma_1, t1=t1, t2=t2, n_pts=250)
        e_emp_50, e_th_50 = evaluate_boundary_l2_energy(s0, primes_50, t1=t1, t2=t2)
        e_emp_100, e_th_100 = evaluate_boundary_l2_energy(s0, primes_100, t1=t1, t2=t2)
        e_emp_300, e_th_300 = evaluate_boundary_l2_energy(s0, primes_300, t1=t1, t2=t2)

        records.append({
            "sigma_0": s0,
            "exact_sum": cw_res["exact_sum"],
            "contour_sum": cw_res["contour_sum"],
            "int_left": cw_res["int_left"],
            "e_emp_100": e_emp_100,
            "e_th_100": e_th_100,
            "e_emp_300": e_emp_300,
            "e_th_300": e_th_300,
            "blowup_factor_th": e_th_300 / (e_th_100 + 1e-12),
        })

    df_results = pd.DataFrame(records)
    df_results.to_csv(output_csv, index=False, encoding="utf-8-sig")
    print(f"          Contour results exported to: {output_csv}")

    # Step 4: Academic Terminal Table Presentation
    print("\n" + "=" * CONSOLE_WIDTH)
    print("  TABLE 1: Littlewood-Jensen Contour & Boundary L2 Energy Across Coordinate sigma_0")
    print("=" * CONSOLE_WIDTH)
    print(f"  {'sigma_0':<8} | {'Exact Zero':<12} | {'Contour Sum':<12} | {'L2 Emp (N=100)':<16} | {'L2 Emp (N=300)':<16} | {'Th. L2 (N=300)'}")
    print("  " + "-" * (CONSOLE_WIDTH - 4))
    for _, r in df_results.iterrows():
        print(
            f"  {r.sigma_0:<8.2f} | {r.exact_sum:<12.4f} | {r.contour_sum:<12.4f} | "
            f"{r.e_emp_100:<16.4f} | {r.e_emp_300:<16.4f} | {r.e_th_300:<16.4e}"
        )
    print("=" * CONSOLE_WIDTH)

    # Step 5: High-Resolution Continuous Scan for Visual Proof
    print("\n[Phase 4] Evaluating continuous scan for publication-grade diagnostics...")
    sigma_dense = np.linspace(0.18, 0.85, 45)
    dense_exact = [max(0.0, 0.50 - s) for s in sigma_dense]
    dense_contour = [evaluate_littlewood_contour(s, sigma_1=sigma_1, t1=t1, t2=t2, n_pts=180)["contour_sum"] for s in sigma_dense]
    
    th_l2_50 = [np.prod(1.0 + primes_50 ** (-2.0 * s)) for s in sigma_dense]
    th_l2_100 = [np.prod(1.0 + primes_100 ** (-2.0 * s)) for s in sigma_dense]
    th_l2_300 = [np.prod(1.0 + primes_300 ** (-2.0 * s)) for s in sigma_dense]

    # Step 6: 4-Panel Publication-Grade Visualization
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))

    # Panel 1: Littlewood-Jensen Phase Boundary Kink at sigma = 1/2
    axes[0, 0].plot(sigma_dense, dense_exact, "k--", lw=2.2, label=r"Exact Ground Truth $\sum(\beta - \sigma_0)$")
    axes[0, 0].plot(sigma_dense, dense_contour, "ro", markersize=4.5, alpha=0.85, label="Contour Integral Evaluation")
    axes[0, 0].axvline(0.5, color="black", linestyle="-.", lw=1.5, label=r"Critical Line $\sigma = 1/2$")
    axes[0, 0].annotate(
        r"Zero Phase Transition Kink ($\sigma = 1/2$)",
        xy=(0.5, 0.0),
        xytext=(0.55, 0.15),
        arrowprops=dict(facecolor="black", shrink=0.08, width=1.2, headwidth=6),
        fontsize=10,
        fontweight="bold",
    )
    axes[0, 0].set_title(r"Littlewood-Jensen Contour Integral $\mathcal{J}(\sigma_0)$", fontsize=12, fontweight="bold")
    axes[0, 0].set_xlabel(r"Left Boundary Coordinate $\sigma_0$")
    axes[0, 0].set_ylabel(r"Zero Sum $\sum_{\rho} (\beta_\rho - \sigma_0)$")
    axes[0, 0].legend(frameon=True, loc="upper right")
    axes[0, 0].grid(True, linestyle="--", alpha=0.5)

    # Panel 2: Theoretical Asymptotic L2 Energy Density (Log Scale)
    axes[0, 1].semilogy(sigma_dense, th_l2_50, color="#2980b9", lw=1.8, label="N = 50 Primes")
    axes[0, 1].semilogy(sigma_dense, th_l2_100, color="#27ae60", lw=1.8, label="N = 100 Primes")
    axes[0, 1].semilogy(sigma_dense, th_l2_300, color="#c0392b", lw=2.2, label="N = 300 Primes")
    axes[0, 1].axvline(0.5, color="black", linestyle="-.", lw=1.5, label=r"Critical Line $\sigma = 1/2$")
    axes[0, 1].set_title(r"Theoretical Ergodic L2 Energy $\prod_{p} (1 + p^{-2\sigma_0})$", fontsize=12, fontweight="bold")
    axes[0, 1].set_xlabel(r"Left Boundary Coordinate $\sigma_0$")
    axes[0, 1].set_ylabel(r"L2 Energy Density (Log Scale)")
    axes[0, 1].legend(frameon=True, loc="upper right")
    axes[0, 1].grid(True, which="both", linestyle="--", alpha=0.5)

    # Panel 3: Empirical L2 Energy on the Finite Contour [12, 16]
    s_sub = df_results["sigma_0"]
    axes[1, 0].plot(s_sub, df_results["e_emp_100"], "s-", color="#27ae60", lw=2.0, label="Empirical N = 100 Primes")
    axes[1, 0].plot(s_sub, df_results["e_emp_300"], "o-", color="#c0392b", lw=2.0, label="Empirical N = 300 Primes")
    axes[1, 0].set_yscale("log")
    axes[1, 0].axvline(0.5, color="black", linestyle="-.", lw=1.5, label=r"Critical Line $\sigma = 1/2$")
    axes[1, 0].set_title(r"Empirical Boundary L2 Energy on Segment $s \in [\sigma_0 + 12i, \sigma_0 + 16i]$", fontsize=12, fontweight="bold")
    axes[1, 0].set_xlabel(r"Left Boundary Coordinate $\sigma_0$")
    axes[1, 0].set_ylabel(r"Empirical Energy $\langle|\mathcal{P}_X|^2\rangle$ (Log Scale)")
    axes[1, 0].legend(frameon=True, loc="upper right")
    axes[1, 0].grid(True, which="both", linestyle="--", alpha=0.5)

    # Panel 4: Prime Scaling Ratio (N=300 / N=100) Demonstrating Divergence
    ratio_th = np.array(th_l2_300) / np.array(th_l2_100)
    axes[1, 1].semilogy(sigma_dense, ratio_th, color="#8e44ad", lw=2.2, label=r"Energy Ratio: $\mathcal{E}_{300}(\sigma_0) / \mathcal{E}_{100}(\sigma_0)$")
    axes[1, 1].axvline(0.5, color="black", linestyle="-.", lw=1.5, label=r"Critical Line $\sigma = 1/2$")
    axes[1, 1].axhline(1.0, color="gray", linestyle=":", lw=1.2, label="Unitary Invariance Ratio = 1.0")
    axes[1, 1].set_title(r"Scaling Explosion Ratio: Divergence for $\sigma_0 < 1/2$", fontsize=12, fontweight="bold")
    axes[1, 1].set_xlabel(r"Left Boundary Coordinate $\sigma_0$")
    axes[1, 1].set_ylabel("Scaling Ratio (Log Scale)")
    axes[1, 1].legend(frameon=True, loc="upper right")
    axes[1, 1].grid(True, which="both", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.savefig(output_png, dpi=300)
    total_time = time.perf_counter() - t_start_global
    print(f"\n[Output] High-resolution diagnostic visualization saved: {output_png}")
    print(f"[Execution] Script 06 completed successfully in {total_time:.2f} seconds.")
    plt.show()


if __name__ == "__main__":
    run_pipeline(
        output_csv="06_carleman_contour_results.csv",
        output_png="06_carleman_contour_analysis.png",
    )