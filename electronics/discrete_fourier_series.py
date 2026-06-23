"""Discrete Fourier Series (DFS) — discrete-time, periodic signal."""
import numpy as np
import matplotlib.pyplot as plt

# Example: periodic square wave (period N)
N = 16
n = np.arange(N)
x = np.array([1 if i < N // 4 else 0 for i in n], dtype=float)

# DFS coefficients: X[k] = sum_{n=0}^{N-1} x[n] * e^{-j2πkn/N}
k = np.arange(N)
X = np.array([np.sum(x * np.exp(-1j * 2 * np.pi * ki * n / N)) for ki in k])

# Reconstruct one period
x_rec = np.array([
    (1 / N) * np.sum(X * np.exp(1j * 2 * np.pi * k * ni / N))
    for ni in n
]).real

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))
ax1.stem(n, x)
ax1.set(title="x[n] (one period)", xlabel="n")

ax2.stem(k, np.abs(X))
ax2.set(title="|X[k]| — DFS Coefficients", xlabel="k")

ax3.stem(n, x_rec)
ax3.set(title="Reconstructed x[n]", xlabel="n")

plt.tight_layout()
plt.show()
