"""Discrete Cosine Transform (DCT) — all 4 types + compression demo."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dct, idct

N = 64
n = np.arange(N)

# Example: smooth signal + noise
x = np.sin(2 * np.pi * 3 * n / N) + 0.3 * np.cos(2 * np.pi * 10 * n / N)

# All 4 DCT types
types = [1, 2, 3, 4]
dct_results = {t: dct(x, type=t, norm='ortho') for t in types}

# Compression demo using DCT-II: keep top-k coefficients
def compress(x, keep):
    c = dct(x, type=2, norm='ortho')
    c[keep:] = 0
    return idct(c, type=2, norm='ortho')

fig, axes = plt.subplots(3, 2, figsize=(12, 9))

axes[0, 0].plot(n, x)
axes[0, 0].set(title="Original Signal x[n]", xlabel="n")

for i, t in enumerate(types):
    ax = axes[(i + 1) // 2, (i + 1) % 2]
    ax.stem(dct_results[t][:32])
    ax.set(title=f"DCT-{t} Coefficients", xlabel="k")

axes[2, 0].plot(n, x, label="Original")
for k in [4, 8, 16]:
    axes[2, 0].plot(n, compress(x, k), '--', label=f"keep={k}")
axes[2, 0].set(title="DCT-II Compression", xlabel="n")
axes[2, 0].legend(fontsize=7)

axes[2, 1].axis('off')

plt.tight_layout()
plt.show()
