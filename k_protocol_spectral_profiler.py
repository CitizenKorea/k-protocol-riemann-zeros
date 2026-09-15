"""
K-PROTOCOL: Riemann-Siegel Baseline Calibrator & Prime Spectral Profiler
Target: Selected Landmark Riemann Zeros (1..10, 20, 40, 60, 80, 100)
Framework: A Citizen of the Republic of Korea (estake@naver.com)
Date: September 2026
"""

import time
import matplotlib.pyplot as plt
import mpmath
import numpy as np
import pandas as pd
from scipy import optimize as opt

# =========================================================================
# 1. Arbitrary-Precision Configuration
# =========================================================================
mpmath.mp.dps = 25
CONSOLE_WIDTH = 86

print("=" * CONSOLE_WIDTH)
print("  K-PROTOCOL: RIEMANN-SIEGEL BASELINE CALIBRATOR & PRIME SPECTRAL PROFILER")
print("  Macro-Baseline Anchor Calibration & Microscopic Phase Profiling")
print("=" * CONSOLE_WIDTH)


# =========================================================================
# 2. Optimized Prime Sieve Generator (100 Primes)
# =========================================================================
def get_primes(n: int) -> np.ndarray:
    """Generates the first n prime numbers using an optimized boolean sieve."""
    primes = []
    sieve = np.ones(n * 15, dtype=bool)
    for p in range(2, len(sieve)):
        if sieve[p]:
            primes.append(p)
            if len(primes) == n:
                break
            sieve[p * p :: p] = False
    return np.array(primes, dtype=np.float64)


primes_pool = get_primes(100)


# =========================================================================
# 3. Macro Riemann-Siegel Phase Angle theta(t)
# =========================================================================
def rs_theta(t: float) -> float:
    """Computes the classical Riemann-Siegel asymptotic phase angle theta(t)."""
    return (
        (t / 2.0) * np.log(t / (2.0 * np.pi))
        - t / 2.0
        - np.pi / 8.0
        + 1.0 / (48.0 * t)
    )


# =========================================================================
# 4. Macroscopic Benchmark Wave Function Z(t)
# =========================================================================
def riemann_siegel_z(t: float) -> float:
    """Evaluates the classical Riemann-Siegel Z(t) expansion.

    Provides the high-precision macroscopic benchmark anchor prior to
    microscopic prime phase cross-decomposition.
    """
    m = int(np.floor(np.sqrt(t / (2.0 * np.pi))))
    th = rs_theta(t)
    n = np.arange(1, m + 1)
    main_sum = 2.0 * np.sum((1.0 / np.sqrt(n)) * np.cos(th - t * np.log(n)))

    # First-order asymptotic boundary remainder R(t)
    p_frac = np.sqrt(t / (2.0 * np.pi)) - m
    c0 = np.cos(2.0 * np.pi * (p_frac**2 - p_frac - 1.0 / 16.0)) / np.cos(
        2.0 * np.pi * p_frac
    )
    r_term = ((-1) ** (m - 1)) * ((t / (2.0 * np.pi)) ** (-0.25)) * c0
    return main_sum + r_term


# =========================================================================
# 5. Dominant Prime Pair Profiler
# =========================================================================
def profile_dominant_prime_pair(t_target: float, primes: np.ndarray):
    """Profiles the Rank 1 destructive prime pair at the calibrated coordinate."""
    P = primes[:30, None]
    Q = primes[None, :30]
    mask = np.triu_indices(30, k=1)
    p_v = P[mask[0], 0]
    q_v = Q[0, mask[1]]
    amp = 2.0 / (p_v * q_v)
    phase = np.cos(t_target * np.log(p_v / q_v))
    impact = amp * phase
    best_i = np.argmin(impact)
    return (
        f"({int(p_v[best_i])}, {int(q_v[best_i])})",
        phase[best_i],
        impact[best_i],
        int(p_v[best_i]),
        int(q_v[best_i]),
    )


# =========================================================================
# 6. Baseline Calibration & Spectral Profiling Engine
# =========================================================================
def calibrate_and_profile_zeros(
    target_indices,
    output_csv="k_protocol_calibrated_sample.csv",
    output_png="k_protocol_spectral_profiler.png",
):
    print(f"  Target Benchmark Zeros : {len(target_indices)} Coordinates: {target_indices}")
    print("  Baseline Calibration   : Brent's Method on Riemann-Siegel Z(t) (xtol = 1e-8)")
    print("  Critical Line Abscissa : Re(s) = 1/2")
    print("-" * CONSOLE_WIDTH)

    results = []
    t_start = time.perf_counter()

    for idx in target_indices:
        # Step 1: True Coordinate Baseline from mpmath
        true_t = float(mpmath.zetazero(idx).imag)

        # Step 2: High-Precision Macro Calibration via Riemann-Siegel
        bracket = [true_t - 0.4, true_t + 0.4]
        sol = opt.root_scalar(
            riemann_siegel_z, bracket=bracket, method="brentq", xtol=1e-8
        )
        rs_t = sol.root

        # Step 3: First-Order Remainder Error Metrics
        rs_err = abs(rs_t - true_t)
        rel_err_pct = (rs_err / true_t) * 100.0

        # Step 4: Microscopic Prime Pair Fingerprinting at Calibrated Coordinate
        pair_str, cos_val, imp_val, p, q = profile_dominant_prime_pair(
            rs_t, primes_pool
        )

        results.append({
            "zero_idx": idx,
            "true_t": true_t,
            "rs_t": rs_t,
            "rs_err": rs_err,
            "rel_err_pct": rel_err_pct,
            "pair_str": pair_str,
            "phase_cos": cos_val,
            "impact_score": imp_val,
            "p": p,
            "q": q,
        })

    df = pd.DataFrame(results)
    df.to_csv(output_csv, index=False, encoding="utf-8-sig")

    # Structured Terminal Output
    print(f"\n  {'Zero #':<7} | {'True t':<12} | {'RS Anchor t':<12} | {'RS Error':<11} | {'Rel Err (%)':<11} | {'Leader':<10} | {'Phase cos':<11} | {'Impact Score'}")
    print("  " + "-" * (CONSOLE_WIDTH - 4))
    for _, r in df.iterrows():
        print(f"  #{r.zero_idx:<6d} | {r.true_t:<12.6f} | {r.rs_t:<12.6f} | {r.rs_err:<11.4e} | {r.rel_err_pct:<11.4f}% | {r.pair_str:<10} | {r.phase_cos:<11.6f} | {r.impact_score:<12.6f}")
    print("=" * CONSOLE_WIDTH)

    print("\n" + "=" * CONSOLE_WIDTH)
    print("  CALIBRATION BASELINE SUMMARY STATISTICS")
    print("=" * CONSOLE_WIDTH)
    print(f"  Mean Absolute Error (RS Baseline) : {df['rs_err'].mean():.6e}")
    print(f"  Median Absolute Error             : {df['rs_err'].median():.6e}")
    print(f"  Minimum Absolute Error            : {df['rs_err'].min():.6e} (Zero #{df.loc[df['rs_err'].idxmin(), 'zero_idx']})")
    print(f"  Maximum Absolute Error            : {df['rs_err'].max():.6e} (Zero #{df.loc[df['rs_err'].idxmax(), 'zero_idx']})")
    print(f"  Mean Relative Error Rate          : {df['rel_err_pct'].mean():.6f}%")
    print(f"  Total Calibration Time            : {time.perf_counter() - t_start:.2f} seconds")
    print("=" * CONSOLE_WIDTH)

    # Visualization
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
    fig, axes = plt.subplots(2, 2, figsize=(14, 11))

    # Panel 1: Riemann-Siegel Calibration Wave
    t_fine = np.linspace(13.0, 15.5, 300)
    z_fine = [riemann_siegel_z(t) for t in t_fine]
    axes[0, 0].plot(t_fine, z_fine, color="#1f4e79", lw=2.2, label=r"Riemann-Siegel $Z(t)$")
    axes[0, 0].axhline(0, color="black", linestyle="--", lw=1.2, alpha=0.7)
    t1_true = df.loc[0, "true_t"]
    t1_rs = df.loc[0, "rs_t"]
    axes[0, 0].scatter([t1_rs], [0], color="#c0392b", s=80, zorder=5, label=f"Calibrated Anchor $\\tilde{{t}}_1 = {t1_rs:.4f}$")
    axes[0, 0].axvline(t1_true, color="#27ae60", linestyle=":", lw=1.5, label=f"True Baseline $t_1 = {t1_true:.4f}$")
    axes[0, 0].set_title(r"Riemann-Siegel Macro-Baseline Calibration ($t_1 \approx 14.1347$)", fontsize=12, fontweight="bold")
    axes[0, 0].set_xlabel("Imaginary Vertical Coordinate (t)")
    axes[0, 0].set_ylabel(r"Macro Wave Amplitude $Z(t)$")
    axes[0, 0].legend(frameon=True, loc="upper right")
    axes[0, 0].grid(True, linestyle="--", alpha=0.5)

    # Panel 2: RS Calibration Residual
    x_labels = [f"#{row['zero_idx']}" for _, row in df.iterrows()]
    x_pos = np.arange(len(df))
    axes[0, 1].semilogy(x_pos, df["rs_err"], color="#c0392b", marker="o", lw=1.8, markersize=5, label=r"Residual $|\tilde{t}_k - t_k| \sim \mathcal{O}(t^{-3/4})$")
    axes[0, 1].axhline(df["rs_err"].mean(), color="#2980b9", linestyle="--", lw=1.5, label=f"Mean Error: {df['rs_err'].mean():.2e}")
    axes[0, 1].set_xticks(x_pos)
    axes[0, 1].set_xticklabels(x_labels, rotation=45, fontsize=9)
    axes[0, 1].set_title("Riemann-Siegel Baseline Residual Across Benchmarks", fontsize=12, fontweight="bold")
    axes[0, 1].set_xlabel("Riemann Zero Index (k)")
    axes[0, 1].set_ylabel("Calibration Error (Log Scale)")
    axes[0, 1].legend(frameon=True, loc="upper right")
    axes[0, 1].grid(True, which="both", linestyle="--", alpha=0.5)

    # Panel 3: Phase Cosine Alignment of Leaders
    axes[1, 0].bar(x_pos, df["phase_cos"], color="#d9534f", width=0.55, edgecolor="none", alpha=0.85, label=r"$\cos(t_k \ln(p/q))$")
    axes[1, 0].axhline(-1.0, color="black", linestyle="--", lw=1.8, label="Anti-Phase Limit (-1.0)")
    axes[1, 0].axhline(-0.9, color="#2c3e50", linestyle=":", lw=1.5, label="Condensation Floor (-0.90)")
    axes[1, 0].set_xticks(x_pos)
    axes[1, 0].set_xticklabels(x_labels, rotation=45, fontsize=9)
    axes[1, 0].set_ylim(-1.05, 0.0)
    axes[1, 0].set_title("Phase Cosine Condensation of Dominant Pairs", fontsize=12, fontweight="bold")
    axes[1, 0].set_xlabel("Riemann Zero Index (k)")
    axes[1, 0].set_ylabel("Phase Cosine Value")
    axes[1, 0].legend(frameon=True, loc="lower right")
    axes[1, 0].grid(True, linestyle="--", alpha=0.5)

    # Panel 4: Impact Score Breakdown
    axes[1, 1].bar(x_pos, df["impact_score"], color="#2b5c8f", width=0.55, edgecolor="none", alpha=0.85)
    for i, row in df.iterrows():
        axes[1, 1].annotate(
            row["pair_str"],
            (i, row["impact_score"]),
            textcoords="offset points",
            xytext=(0, -14),
            ha="center",
            fontsize=7.5,
            fontweight="bold",
            color="#1f4e79",
        )
    axes[1, 1].set_xticks(x_pos)
    axes[1, 1].set_xticklabels(x_labels, rotation=45, fontsize=9)
    axes[1, 1].set_ylim(df["impact_score"].min() * 1.25, 0.02)
    axes[1, 1].set_title("Rank 1 Impact Score and Profiling Fingerprint", fontsize=12, fontweight="bold")
    axes[1, 1].set_xlabel("Riemann Zero Index (k)")
    axes[1, 1].set_ylabel(r"Impact Score $\mathcal{M}_{pq} = \frac{2}{pq}\cos\phi$")
    axes[1, 1].grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.savefig(output_png, dpi=300)
    print(f"\n[Output] Diagnostic plot saved: {output_png}")
    print(f"[Output] Baseline validation CSV saved: {output_csv}")
    plt.show()


if __name__ == "__main__":
    targets = list(range(1, 11)) + [20, 40, 60, 80, 100]
    calibrate_and_profile_zeros(targets)