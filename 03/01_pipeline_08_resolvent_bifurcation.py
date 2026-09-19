"""
===============================================================================
K-Protocol: Quantum Many-Body Prime Phase Interference Pipeline
Module: Real Asymmetric Resolvent Operator and Complex Spectral Bifurcation
Repository: https://github.com/CitizenKorea/k-protocol-riemann-zeros
===============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

def generate_primes(count: int) -> np.ndarray:
    """Generate the first N prime numbers via trial division."""
    primes = []
    num = 2
    while len(primes) < count:
        if all(num % p != 0 for p in primes):
            primes.append(num)
        num += 1
    return np.array(primes, dtype=np.float64)

# 1. System Parameters
N_PRIMES = 40
primes = generate_primes(N_PRIMES)

ln_p = np.log(primes)
ln_diff = ln_p[:, None] - ln_p[None, :]
inv_sqrt_pp = 1.0 / np.sqrt(primes[:, None] * primes[None, :])
inv_p = 1.0 / primes

def build_asymmetric_hamiltonian(sigma: float, t: float) -> np.ndarray:
    """
    Constructs the real asymmetric reflection gauge operator H(s) = K + Gamma.
    - K: Symmetric coherent interference tensor
    - Gamma: Skew-symmetric hyperbolic reflection tensor
    Strictly real symmetric if and only if sigma = 0.5 (delta = 0).
    """
    delta = sigma - 0.5
    
    # Coherent symmetric interaction
    K = inv_sqrt_pp * np.cos(t * ln_diff)
    np.fill_diagonal(K, inv_p)
    
    # Hyperbolic skew-symmetric gauge tensor
    Gamma = inv_sqrt_pp * np.sinh(delta * ln_diff)
    np.fill_diagonal(Gamma, 0.0)
    
    return K + Gamma

# 2. Calibration of Target Resonance Energy (t_1 ~ 14.134725)
t_target = 14.134725
H_target = build_asymmetric_hamiltonian(0.5, t_target)
target_eigs = np.linalg.eigvalsh(H_target)
E_0 = np.max(target_eigs)

print("=" * 65)
print(f"[*] Pipeline Actuated: Resonance Calibration at t = {t_target:.6f}")
print(f"[*] Ground State Resonance Energy Level E_0 = {E_0:.6f}")
print("=" * 65)

# 3. Task A: Complex Spectral Bifurcation Tracking (Spectral Flow)
sigma_steps = 150
sigma_vals = np.linspace(0.5, 0.7, sigma_steps)
all_eigvals = np.zeros((sigma_steps, N_PRIMES), dtype=complex)

for idx, s_val in enumerate(sigma_vals):
    H = build_asymmetric_hamiltonian(s_val, t_target)
    all_eigvals[idx, :] = np.linalg.eigvals(H)

# 4. Task B: 2D Resolvent Minimum Singular Value Landscape
sigma_grid = np.linspace(0.2, 0.8, 60)
t_grid = np.linspace(12.0, 16.0, 60)
resolvent_sv_map = np.zeros((len(t_grid), len(sigma_grid)))
I_N = np.eye(N_PRIMES)

for i, t_val in enumerate(t_grid):
    for j, s_val in enumerate(sigma_grid):
        H = build_asymmetric_hamiltonian(s_val, t_val)
        resolvent_op = H - E_0 * I_N
        resolvent_sv_map[i, j] = np.min(np.linalg.svd(resolvent_op, compute_uv=False))

# 5. Diagnostic Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Panel 1: Pitchfork Bifurcation in Complex Plane
for k in range(N_PRIMES):
    ax1.plot(all_eigvals[:, k].real, all_eigvals[:, k].imag, 
             lw=1.5, alpha=0.7, color='teal')

ax1.scatter(all_eigvals[0, :].real, all_eigvals[0, :].imag, 
            color='red', s=40, zorder=5, label=r'$\sigma = 0.50$ (Strict Real Spectrum)')
ax1.scatter(all_eigvals[-1, :].real, all_eigvals[-1, :].imag, 
            color='blue', s=30, zorder=5, label=r'$\sigma = 0.70$ (Complex Conjugate Pairs)')

ax1.axhline(0, color='black', lw=1.2, ls='--')
ax1.set_title(r'Real Asymmetric Complex Bifurcation ($t = 14.13$)', fontsize=12)
ax1.set_xlabel(r'$\mathrm{Re}(\lambda)$', fontsize=11)
ax1.set_ylabel(r'$\mathrm{Im}(\lambda)$', fontsize=11)
ax1.grid(True, ls=":", alpha=0.6)
ax1.legend(loc='upper left', fontsize=10)

# Panel 2: 2D Resolvent Resonance Funnel
c = ax2.contourf(sigma_grid, t_grid, resolvent_sv_map, levels=40, cmap='viridis_r')
cbar = fig.colorbar(c, ax=ax2)
cbar.set_label(r'Resolvent Minimum Singular Value $\sigma_{\min}(H - E_0 I)$', fontsize=10)

ax2.axvline(0.5, color='red', linestyle='--', lw=2, label=r'Critical Axis $\sigma = 0.5$')
ax2.scatter([0.5], [t_target], color='white', s=90, edgecolors='black', 
            label=f'Target Zero ({t_target:.2f})', zorder=6)

ax2.set_title(r'2D Resolvent Resonance Funnel (Singular Well)', fontsize=12)
ax2.set_xlabel(r'Real Coordinate $\sigma$', fontsize=11)
ax2.set_ylabel(r'Imaginary Coordinate $t$', fontsize=11)
ax2.legend(loc='upper right', fontsize=10)

plt.tight_layout()
plt.savefig("resolvent_resonance_bifurcation.png", dpi=300)
plt.show()

print("[+] Execution Completed: Figure saved as 'resolvent_resonance_bifurcation.png'.")