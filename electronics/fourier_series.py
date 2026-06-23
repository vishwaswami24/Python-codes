"""Fourier Series — continuous, periodic signals."""
import numpy as np
import matplotlib.pyplot as plt

T = 2 * np.pi          # period
N = 10                 # number of harmonics
t = np.linspace(0, 2 * T, 1000)

# Example: square wave (odd harmonics only)
def square_wave(t, T):
    return np.sign(np.sin(2 * np.pi * t / T))

x = square_wave(t, T)

# Fourier coefficients via numerical integration
def fourier_coeff(n, x, t, T):
    dt = t[1] - t[0]
    return (1 / T) * np.sum(x * np.exp(-1j * 2 * np.pi * n * t / T)) * dt

coeffs = {n: fourier_coeff(n, x, t, T) for n in range(-N, N + 1)}

# Reconstruct from series
x_reconstructed = sum(cn * np.exp(1j * 2 * np.pi * n * t / T) for n, cn in coeffs.items()).real

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
ax1.plot(t, x, label="Original"), ax1.plot(t, x_reconstructed, '--', label=f"N={N}")
ax1.set(title="Fourier Series Reconstruction", xlabel="t")
ax1.legend()

ns = list(coeffs.keys())
ax2.stem(ns, [np.abs(coeffs[n]) for n in ns])
ax2.set(title="Spectrum |c_n|", xlabel="n (harmonic)")

plt.tight_layout()
plt.show()
