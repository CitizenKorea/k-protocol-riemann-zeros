"""
========================================================================================
K-PROTOCOL: EULER-MACLAURIN TAIL COUPLING & SUB-CRITICAL STABILITY TEST
Script: 05_euler_maclaurin_tail_test.py
Target: Benchmark Zero #100 (t ~ 236.5242) Across Real Coordinates sigma in [0.15, 0.85]
Physical Derivation: Inability of Macroscopic Tail to Restore Sub-Critical Decoupling
Author: A Citizen of the Republic of Korea (estake@naver.com)
Date: September 2026
License: Creative Commons Attribution 4.0 International (CC BY 4.0)
========================================================================================
"""

import math
import time
import matplotlib.pyplot as plt
import mpmath
import numpy as np
import pandas as pd
from scipy.special import bernoulli

# =========================================================================
# 1. High-Precision Precision Configuration & Terminal Banner
# =========================================================================
mpmath.mp.dps = 25
CONSOLE_WIDTH = 92

print("=" * CONSOLE_WIDTH)
print("  K-PROTOCOL: EULER-MACLAURIN TAIL COUPLING & SUB-CRITICAL STABILITY TEST")
print("  Evaluating Macro-Tail Compensation vs. Micro-Prime Decoupling Breakdown")
print("=" * CONSOLE_WIDTH)


# =========================================================================
# 2. Optimized Boolean Sieve for Generating Prime Oscillators (100 Primes)
# =========================================================================
def generate_prime_ensemble(n: int = 100) -> np.ndarray:
    """Generates the first n prime numbers using an optimized boolean sieve."""
    primes = []
    sieve_size = max(2000, n * 15)
    sieve = np.ones(sieve_size, dtype=bool)
    for p in range(2, len(sieve)):
        if sieve[p]:
            primes.append(p)
            if len(primes) == n:
                break
            sieve[p * p :: p] = False
    return np.array(primes, dtype=np.float64)


# =========================================================================
# 3. Analytic Continuation: Euler-Maclaurin Remainder Tail Function
# =========================================================================
def compute_euler_maclaurin_tail(s_complex: complex, cutoff_x: float, m_orders: int = 3) -> complex:
    """Computes the asymptotic remainder tail T_M(s, X) of the truncated Dirichlet series.
    
    zeta(s) = sum_{n <= X} n^{-s} + T_M(s, X)
    where T_M(s, X) = X^{1-s}/(s-1) - 0.5*X^{-s} + sum_{k=1}^m B_{2k}/(2k)! * s(s+1)...*X^{-(s+2k-1)}
    """
    # 1. Leading integral term: X^{1-s} / (s - 1)
    integral_term = (cutoff_x ** (1.0 - s_complex)) / (s_complex - 1.0)

    # 2. First boundary correction term: - 0.5 * X^{-s}
    boundary_term = -0.5 * (cutoff_x ** (-s_complex))

    # 3. Higher-order Bernoulli terms
    b_coeffs = bernoulli(2 * m_orders + 2)
    bernoulli_sum = 0.0 + 0.0j
    s_prod = s_complex

    for k in range(1, m_orders + 1):
        coeff = b_coeffs[2 * k] / math.factorial(2 * k)
        term = coeff * s_prod * (cutoff_x ** (-(s_complex + 2 * k - 1)))
        bernoulli_sum += term
        s_prod *= (s_complex + 2 * k - 1) * (s_complex + 2 * k)

    return integral_term + boundary_term + bernoulli_sum


# =========================================================================
# 4. Multi-Particle Generating Polynomial with Tail Coupling
# =========================================================================
def compute_tail_coupled_saturation(
    t_val: float,
    primes_arr: np.ndarray,
    sigma: float = 0.5,
    max_k: int = 5,
    m_orders: int = 3,
):
    """Evaluates 5-body saturation for pure prime lattice vs. macro-tail coupled lattice."""
    s_complex = sigma + 1j * t_val
    cutoff_x = primes_arr[-1]
    log_p = np.log(primes_arr)
    x = (primes_arr ** -sigma) * np.exp(-1j * t_val * log_p)

    # A. Pure micro-prime multi-particle generating polynomial
    poly_prime = np.array([1.0 + 0j], dtype=np.complex128)
    for val in x:
        new_p = np.zeros(len(poly_prime) + 1, dtype=np.complex128)
        new_p[:-1] += poly_prime
        new_p[1:] += poly_prime * val
        poly_prime = new_p

    mags_prime_sq = np.abs(poly_prime[1:]) ** 2
    tot_e_prime = np.sum(mags_prime_sq)
    sat_prime = np.cumsum(mags_prime_sq) / tot_e_prime * 100.0

    # B. Compute Euler-Maclaurin analytic continuation tail
    tail = compute_euler_maclaurin_tail(s_complex, cutoff_x=cutoff_x, m_orders=m_orders)

    # C. Couple macroscopic tail as an effective background degree of freedom
    # P_coupled(z) = P_prime(z) * (1 + T_M * z)
    poly_coupled = np.zeros(len(poly_prime) + 1, dtype=np.complex128)
    poly_coupled[:-1] += poly_prime
    poly_coupled[1:] += poly_prime * tail

    mags_coupled_sq = np.abs(poly_coupled[1:]) ** 2
    tot_e_coupled = np.sum(mags_coupled_sq)
    sat_coupled = np.cumsum(mags_coupled_sq) / tot_e_coupled * 100.0

    return (
        sat_prime[max_k - 1],
        sat_coupled[max_k - 1],
        np.abs(tail),
        np.abs(poly_prime[1]),
        sat_prime[:10],
        sat_coupled[:10],
    )


# =========================================================================
# 5. Core Execution Pipeline
# =========================================================================
def run_pipeline(
    output_csv: str = "05_euler_maclaurin_tail_results.csv",
    output_png: str = "05_euler_maclaurin_tail_analysis.png",
):
    t_start_global = time.perf_counter()

    # Step 1: Prime Ensemble Initialization
    primes = generate_prime_ensemble(100)
    cutoff_x = primes[-1]
    print(f"\n[Phase 1] Prime ensemble initialized (N=100 primes, Cutoff X = {cutoff_x:.0f})...")

    # Step 2: Target Zero Acquisition (Zero #100: t ~ 236.5242)
    t_target = float(mpmath.zetazero(100).imag)
    print(f"[Phase 2] Benchmark zero selected: Zero #100 at t = {t_target:.6f}")

    # Step 3: Discrete Parameter Sweep Across Coordinate sigma
    sigma_discrete = [0.20, 0.30, 0.40, 0.45, 0.50, 0.55, 0.60, 0.70, 0.80]
    discrete_records = []

    print("\n[Phase 3] Scanning discrete sigma coordinates with macro-tail coupling...")
    for sig in sigma_discrete:
        sat_p, sat_c, tail_norm, prime_1b, _, _ = compute_tail_coupled_saturation(
            t_target, primes, sigma=sig, max_k=5, m_orders=3
        )
        discrete_records.append({
            "sigma": sig,
            "sat_prime": sat_p,
            "sat_coupled": sat_c,
            "delta_sat": sat_c - sat_p,
            "tail_norm": tail_norm,
            "prime_1b": prime_1b,
            "tail_to_1b_ratio": tail_norm / prime_1b,
        })

    df_discrete = pd.DataFrame(discrete_records)
    df_discrete.to_csv(output_csv, index=False, encoding="utf-8-sig")
    print(f"          Discrete scan exported to: {output_csv}")

    # Step 4: Academic Terminal Table Presentation
    print("\n" + "=" * CONSOLE_WIDTH)
    print("  TABLE 1: Euler-Maclaurin Tail Compensation Test Across Real Coordinate sigma")
    print("=" * CONSOLE_WIDTH)
    print(f"  {'sigma':<6} | {'Pure Prime k<=5':<16} | {'Tail-Coupled k<=5':<18} | {'Tail Norm |T|':<15} | {'Stability Verdict'}")
    print("  " + "-" * (CONSOLE_WIDTH - 4))
    for _, r in df_discrete.iterrows():
        verdict = "EFT Decoupled (>99%)" if r.sat_coupled >= 99.0 else "Catastrophic Breakdown"
        print(f"  {r.sigma:<6.2f} | {r.sat_prime:14.4f}%  | {r.sat_coupled:16.4f}%   | {r.tail_norm:<15.4e} | {verdict}")
    print("=" * CONSOLE_WIDTH)

    # Step 5: Dense Continuous Scan for Publication-Grade Diagnostics
    print("\n[Phase 4] Computing high-resolution continuous scan (sigma in [0.15, 0.85])...")
    sigma_dense = np.linspace(0.15, 0.85, 71)
    dense_prime = []
    dense_coupled = []
    dense_tail = []

    for sig in sigma_dense:
        sp, sc, tn, _, _, _ = compute_tail_coupled_saturation(t_target, primes, sigma=sig, max_k=5, m_orders=3)
        dense_prime.append(sp)
        dense_coupled.append(sc)
        dense_tail.append(tn)

    dense_prime = np.array(dense_prime)
    dense_coupled = np.array(dense_coupled)
    dense_tail = np.array(dense_tail)

    # Step 6: 4-Panel Publication-Grade Visualization
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))

    # Panel 1: Pure Prime vs Tail-Coupled Saturation Across sigma
    axes[0, 0].plot(sigma_dense, dense_prime, "b-", lw=2.0, label=r"Pure Prime Lattice ($k \leq 5$)")
    axes[0, 0].plot(sigma_dense, dense_coupled, "r--", lw=2.0, label=r"Tail-Coupled Lattice ($k \leq 5$)")
    axes[0, 0].axvline(0.5, color="black", linestyle="-.", lw=1.8, label=r"Critical Line $\sigma = 1/2$")
    axes[0, 0].axhline(99.0, color="gray", linestyle=":", lw=1.5, label="99.0% EFT Cutoff Floor")
    axes[0, 0].set_title(r"5-Body Saturation: Macro-Tail Coupling vs. Real Coordinate $\sigma$", fontsize=12, fontweight="bold")
    axes[0, 0].set_xlabel(r"Real Abscissa Coordinate $\sigma$")
    axes[0, 0].set_ylabel(r"Cumulative Saturation $k \leq 5$ (%)")
    axes[0, 0].set_ylim(15, 102)
    axes[0, 0].legend(frameon=True, loc="lower right")
    axes[0, 0].grid(True, linestyle="--", alpha=0.5)

    # Panel 2: Divergence of the Euler-Maclaurin Remainder Tail Norm
    axes[0, 1].semilogy(sigma_dense, dense_tail, color="#8e44ad", lw=2.2, label=r"Macro Tail $|\mathcal{T}_M(s, X)|$")
    axes[0, 1].axvline(0.5, color="black", linestyle="-.", lw=1.8, label=r"Critical Line $\sigma = 1/2$")
    axes[0, 1].set_title(r"Divergence of the Analytic Tail Magnitude for $\sigma < 1/2$", fontsize=12, fontweight="bold")
    axes[0, 1].set_xlabel(r"Real Abscissa Coordinate $\sigma$")
    axes[0, 1].set_ylabel(r"Tail Magnitude $|\mathcal{T}_M|$ (Log Scale)")
    axes[0, 1].legend(frameon=True, loc="upper right")
    axes[0, 1].grid(True, which="both", linestyle="--", alpha=0.5)

    # Panel 3: Coupling Degradation Penalty (Delta Saturation)
    delta_sat = dense_coupled - dense_prime
    axes[1, 0].plot(sigma_dense, delta_sat, color="#c0392b", lw=2.0, label=r"Coupling Penalty $\Delta = \mathrm{Sat}_{\mathrm{coupled}} - \mathrm{Sat}_{\mathrm{pure}}$")
    axes[1, 0].axhline(0.0, color="black", linestyle="--", lw=1.2)
    axes[1, 0].axvline(0.5, color="black", linestyle="-.", lw=1.8, label=r"Critical Line $\sigma = 1/2$")
    axes[1, 0].set_title(r"Destabilization Penalty Induced by Macro-Tail Coupling", fontsize=12, fontweight="bold")
    axes[1, 0].set_xlabel(r"Real Abscissa Coordinate $\sigma$")
    axes[1, 0].set_ylabel(r"Saturation Shift $\Delta$ (%)")
    axes[1, 0].legend(frameon=True, loc="lower right")
    axes[1, 0].grid(True, linestyle="--", alpha=0.5)

    # Panel 4: Multi-Particle Energy Distribution at Sub-Critical Coordinate (sigma = 0.30)
    _, _, _, _, cum_p_03, cum_c_03 = compute_tail_coupled_saturation(t_target, primes, sigma=0.30, max_k=5)
    orders_k = np.arange(1, 11)
    axes[1, 1].plot(orders_k, cum_p_03, "s-", color="#2980b9", lw=1.8, label=r"Pure Primes ($\sigma = 0.30$)")
    axes[1, 1].plot(orders_k, cum_c_03, "o--", color="#e74c3c", lw=1.8, label=r"Tail-Coupled ($\sigma = 0.30$)")
    axes[1, 1].axhline(99.0, color="black", linestyle=":", lw=1.4, label="99.0% Threshold")
    axes[1, 1].axvline(5, color="green", linestyle="-.", lw=1.4, label="5-Body Cutoff ($k=5$)")
    axes[1, 1].set_title(r"Multi-Particle Energy Spread at Sub-Critical Line ($\sigma = 0.30$)", fontsize=12, fontweight="bold")
    axes[1, 1].set_xlabel("Interaction Order (k)")
    axes[1, 1].set_ylabel("Cumulative Spectral Energy (%)")
    axes[1, 1].set_ylim(10, 102)
    axes[1, 1].legend(frameon=True, loc="lower right")
    axes[1, 1].grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.savefig(output_png, dpi=300)
    total_time = time.perf_counter() - t_start_global
    print(f"\n[Output] High-resolution diagnostic visualization saved: {output_png}")
    print(f"[Execution] Script 05 completed successfully in {total_time:.2f} seconds.")
    plt.show()


if __name__ == "__main__":
    run_pipeline(
        output_csv="05_euler_maclaurin_tail_results.csv",
        output_png="05_euler_maclaurin_tail_analysis.png",
    )