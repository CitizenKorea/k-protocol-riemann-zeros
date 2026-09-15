"""
K-PROTOCOL: N-Body Multiscale Spectral Resonance Analyzer
Target: 100th Non-Trivial Riemann Zero (t_100) across Prime Ensembles
Framework: A Citizen of the Republic of Korea (estake@naver.com)
Date: September 2026
"""

import time
import matplotlib.pyplot as plt
import mpmath
import numpy as np
import pandas as pd

# =========================================================================
# 1. Arbitrary-Precision Initialization & Zero Targeting
# =========================================================================
mpmath.mp.dps = 25
CONSOLE_WIDTH = 80

print("=" * CONSOLE_WIDTH)
print("  K-PROTOCOL: N-BODY MULTISCALE SPECTRAL RESONANCE ANALYZER")
print("  Systematic Evaluation: 100th Riemann Zero (t_100) across Prime Ensembles")
print("=" * CONSOLE_WIDTH)

t_global_start = time.perf_counter()
t100 = float(mpmath.zetazero(100).imag)
print(f"  Target Zero Coordinate : t_100 = {t100:.6f}")
print(f"  Critical Line Abscissa : Re(s) = 1/2")
print(f"  Ensemble Truncation    : First 100 Primes (p in [2, 541])")
print("-" * CONSOLE_WIDTH)


# =========================================================================
# 2. Sieve of Eratosthenes Prime Generator
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
    return np.array(primes, dtype=np.int64)


primes = get_primes(100)
primes_float = primes.astype(np.float64)

# =========================================================================
# 3. Phase 1: 2-Body Pairwise Cross-Interference Matrix
# =========================================================================
print("\n[Phase 1] Evaluating Pairwise Cross-Interference Matrix (2-Body Pairs)...")
P = primes_float[:, None]
Q = primes_float[None, :]
mask_2 = np.triu_indices(len(primes), k=1)
p_2 = P[mask_2[0], 0]
q_2 = Q[0, mask_2[1]]

amp_2 = 2.0 / (p_2 * q_2)
phase_2 = np.cos(t100 * np.log(p_2 / q_2))
impact_2 = amp_2 * phase_2
idx_2 = np.argsort(impact_2)[:5]

# =========================================================================
# 4. Phase 2: Composite-Prime Harmonic Couplings (pq vs. r)
# =========================================================================
print("[Phase 2] Evaluating Composite-Prime Harmonic Couplings (pq vs. r)...")
triplets = []
for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        p, q = primes[i], primes[j]
        pq = p * q
        for r in primes:
            if r == p or r == q:
                continue
            ratio = pq / r
            phase = np.cos(t100 * np.log(ratio))
            amp = 2.0 / (pq * r)
            triplets.append((p, q, r, pq, ratio, amp * phase, phase))

df_trip = pd.DataFrame(
    triplets, columns=["p", "q", "r", "pq", "ratio", "impact", "phase"]
)
df_trip_sorted = df_trip.sort_values("impact").head(5).reset_index(drop=True)

# =========================================================================
# 5. Phase 3: N-Body Generating Function Polynomial Convolution
# =========================================================================
print("[Phase 3] Computing N-Body Generating Polynomial Convolution (k = 1..100)...")
t_conv_0 = time.perf_counter()
x = (primes_float**-0.5) * np.exp(-1j * t100 * np.log(primes_float))
poly = np.array([1.0 + 0j])
for val in x:
    new_poly = np.zeros(len(poly) + 1, dtype=np.complex128)
    new_poly[:-1] += poly
    new_poly[1:] += poly * val
    poly = new_poly
conv_elapsed = time.perf_counter() - t_conv_0
print(f"          Convolution completed in {conv_elapsed * 1e3:.3f} ms.")

k_vals = np.arange(1, 101)
magnitudes = np.array([np.abs(poly[k]) for k in k_vals])
energy_sq = magnitudes**2
cum_energy = np.cumsum(energy_sq) / np.sum(energy_sq) * 100.0

# =========================================================================
# 6. Structured Academic Terminal Output
# =========================================================================
print("\n" + "=" * CONSOLE_WIDTH)
print("  TABLE 1: Top 5 Destructive 2-Body Pairs [M_pq = A_pq * cos(t ln(p/q))]")
print("=" * CONSOLE_WIDTH)
print(f"  {'Rank':<6} | {'Pair (p, q)':<14} | {'Phase cos':<14} | {'Impact Score':<16} | {'Spectral Role'}")
print("  " + "-" * (CONSOLE_WIDTH - 4))
for r, i in enumerate(idx_2, start=1):
    pair_str = f"({int(p_2[i])}, {int(q_2[i])})"
    role = "Dominant Anchor" if r == 1 else "Phase Coupler"
    print(f"  {r:<6} | {pair_str:<14} | {phase_2[i]:<14.6f} | {impact_2[i]:<16.6f} | {role:<14}")
print("-" * CONSOLE_WIDTH)

print("\n" + "=" * CONSOLE_WIDTH)
print("  TABLE 2: Top 5 Composite-Prime Harmonic Couplings [M_{pq,r} = A_{pq,r} * cos(t ln(pq/r))]")
print("=" * CONSOLE_WIDTH)
print(f"  {'Rank':<5} | {'(p, q, r)':<13} | {'pq':<6} | {'Ratio (pq/r)':<13} | {'Phase cos':<11} | {'Impact Score':<12}")
print("  " + "-" * (CONSOLE_WIDTH - 4))
for r, row in df_trip_sorted.iterrows():
    trip_str = f"({int(row.p)}, {int(row.q)}, {int(row.r)})"
    print(f"  {r+1:<5} | {trip_str:<13} | {int(row.pq):<6} | {row.ratio:<13.4f} | {row.phase:<11.6f} | {row.impact:<12.6f}")
print("-" * CONSOLE_WIDTH)

print("\n" + "=" * CONSOLE_WIDTH)
print("  TABLE 3: N-Body Coupling Energy Decay Spectrum & Cumulative Saturation")
print("=" * CONSOLE_WIDTH)
print(f"  {'Order (k)':<12} | {'Coupling Magnitude |S_k|':<24} | {'Cumulative Energy (%)':<22} | {'Decoupling Status'}")
print("  " + "-" * (CONSOLE_WIDTH - 4))
status_map = {
    1: "Single-Prime Foundation",
    2: "Pairwise Cross-Lattice",
    3: "Composite-Prime Tuning",
    4: "High-Order Boundary",
    5: "Physical Decoupling Cutoff (>99.8%)",
    6: "Asymptotic Residual Tail",
    10: "Micro-Perturbation Limit",
    20: "Numerically Suppressed",
    50: "Deep Algebraic Decoupling",
    100: "Algebraic Extinction Limit",
}
for k in [1, 2, 3, 4, 5, 6, 10, 20, 50, 100]:
    stat = status_map.get(k, "")
    print(f"  k = {k:<8d} | {magnitudes[k-1]:<24.6e} | {cum_energy[k-1]:<22.4f}% | {stat}")
print("=" * CONSOLE_WIDTH)

total_elapsed = time.perf_counter() - t_global_start
print(f"\n  [Execution Summary] Pipeline execution completed in {total_elapsed:.2f} seconds.")

# =========================================================================
# 7. Publication-Grade 4-Panel Visualization
# =========================================================================
plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
fig, axes = plt.subplots(2, 2, figsize=(14, 11))

# Panel 1: 2-Body vs Composite-Prime Destructive Impact
x_pos = np.arange(5)
width = 0.35
axes[0, 0].bar(x_pos - width / 2, [impact_2[i] for i in idx_2], width, label="2-Body (Pair)", color="#2b5c8f")
axes[0, 0].bar(x_pos + width / 2, df_trip_sorted["impact"], width, label="Composite-Prime (pq/r)", color="#e06d53")
axes[0, 0].set_title("Destructive Impact: 2-Body vs. Composite-Prime Top 5", fontsize=12, fontweight="bold")
axes[0, 0].set_ylabel("Impact Score (Negative Coupling)")
axes[0, 0].set_xticks(x_pos)
axes[0, 0].set_xticklabels([f"Rank {i+1}" for i in range(5)])
axes[0, 0].legend(frameon=True)
axes[0, 0].grid(True, linestyle="--", alpha=0.5)

# Panel 2: Composite-Prime Harmonic Scatter
sample_indices = np.random.choice(len(df_trip), min(3000, len(df_trip)), replace=False)
sample_df = df_trip.iloc[sample_indices]
axes[0, 1].scatter(sample_df["ratio"], sample_df["phase"], alpha=0.15, color="#7f8c8d", s=12, label="Harmonic Samples (N=3000)")
axes[0, 1].scatter(df_trip_sorted["ratio"], df_trip_sorted["phase"], color="#c0392b", s=75, zorder=5, edgecolors="black", label="Top 5 Resonant Snipers")

offsets = [(-22, 12), (25, 12), (0, 12), (0, 12), (0, -18)]
for idx, r in df_trip_sorted.iterrows():
    axes[0, 1].annotate(
        f"({int(r.p)}*{int(r.q)}/{int(r.r)})",
        (r.ratio, r.phase),
        textcoords="offset points",
        xytext=offsets[idx],
        ha="center",
        fontsize=8.5,
        fontweight="bold",
    )
axes[0, 1].set_xscale("log")
axes[0, 1].set_title(r"Composite-Prime Harmonic Couplings: Frequency Ratio ($pq/r$) vs. Phase Cosine", fontsize=12, fontweight="bold")
axes[0, 1].set_xlabel("Resonance Frequency Ratio: pq / r (Log Scale)")
axes[0, 1].set_ylabel(r"$\cos(t_{100} \ln(pq/r))$")
axes[0, 1].axhline(-1.0, color="black", linestyle="--", alpha=0.8, label="Anti-Phase Limit (-1.0)")
axes[0, 1].legend(frameon=True, loc="upper right")
axes[0, 1].grid(True, which="both", linestyle="--", alpha=0.5)

# Panel 3: N-Body Coupling Energy Decay Spectrum
axes[1, 0].semilogy(k_vals, magnitudes, color="#c0392b", lw=2.2, marker="o", markersize=3.5, label=r"Coupling Norm $|S_k(t_{100})|$")
axes[1, 0].axvline(5, color="#2980b9", linestyle="--", lw=1.8, label="Decoupling Cutoff (k = 5)")
axes[1, 0].set_title(r"N-Body Coupling Energy Decay Spectrum ($k = 1 \dots 100$)", fontsize=12, fontweight="bold")
axes[1, 0].set_xlabel("N-Body Interaction Order (k)")
axes[1, 0].set_ylabel("Coupling Magnitude (Log Scale)")
axes[1, 0].grid(True, which="both", linestyle="--", alpha=0.5)
axes[1, 0].legend(frameon=True)

# Panel 4: Cumulative Energy Saturation Curve
axes[1, 1].plot(k_vals[:15], cum_energy[:15], color="#27ae60", lw=2.5, marker="s", markersize=5, label="Cumulative Energy Saturation")
axes[1, 1].axhline(99.8718, color="#e74c3c", linestyle=":", lw=1.8, label="5-Body Cutoff (99.87%)")
for k in [1, 2, 3, 4, 5]:
    axes[1, 1].annotate(
        f"{cum_energy[k-1]:.2f}%",
        (k, cum_energy[k-1]),
        textcoords="offset points",
        xytext=(0, -16),
        ha="center",
        fontsize=8.5,
        fontweight="bold",
    )
axes[1, 1].set_title(r"Cumulative Energy Saturation ($k \leq 15$)", fontsize=12, fontweight="bold")
axes[1, 1].set_xlabel("N-Body Interaction Order (k)")
axes[1, 1].set_ylabel("Cumulative Spectral Energy (%)")
axes[1, 1].set_ylim(50, 102)
axes[1, 1].grid(True, linestyle="--", alpha=0.5)
axes[1, 1].legend(frameon=True, loc="lower right")

plt.tight_layout()
output_fig = "k_protocol_100th_zero_nbody.png"
plt.savefig(output_fig, dpi=300)
print(f"\n[Output] Diagnostic plot saved successfully: {output_fig}")
plt.show()