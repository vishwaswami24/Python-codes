"""Chirp Z-Transform (CZT) — generalized DFT on arbitrary spiral contour in z-plane."""
import numpy as np
import matplotlib.pyplot as plt

def czt(x, M, W, A):
    """
    CZT of x: M output points, starting at A, stepping by W^{-1}.
    Standard DFT: M=N, W=e^{-j2π/N}, A=1.
    """
    N = len(x)
    k = np.arange(M)
    n = np.arange(N)
    # Bluestein's identity: n*k = -(k-n)^2/2 + n^2/2 + k^2/2
    yn = x * A ** -n * W ** (n**2 / 2)
    h  = W ** -(k**2 / 2)
    # convolve yn with h using FFT
    L  = int(2 ** np.ceil(np.log2(N + M - 1)))
    G  = np.fft.ifft(np.fft.fft(yn, L) * np.fft.fft(np.conj(h[:M]), L))
    return G[:M] * W ** (k**2 / 2)

N  = 64
n  = np.arange(N)
x  = np.sin(2 * np.pi * 5 * n / N) + 0.5 * np.sin(2 * np.pi * 20 * n / N)

# --- Standard DFT via CZT ---
M_std = N
W_std = np.exp(-1j * 2 * np.pi / N)
X_czt_std = czt(x, M_std, W_std, A=1.0)
X_fft     = np.fft.fft(x)

# --- Zoom into a narrow frequency band [f1, f2] with high resolution ---
f1, f2 = 0.05, 0.40          # normalized frequencies
M_zoom = 256
W_zoom = np.exp(-1j * 2 * np.pi * (f2 - f1) / M_zoom)
A_zoom = np.exp(1j * 2 * np.pi * f1)
X_zoom = czt(x, M_zoom, W_zoom, A_zoom)
freqs_zoom = np.linspace(f1, f2, M_zoom)

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

axes[0].stem(n, x)
axes[0].set(title="Signal x[n]", xlabel="n")

axes[1].plot(np.arange(N), np.abs(X_fft),   label="FFT", alpha=0.7)
axes[1].plot(np.arange(N), np.abs(X_czt_std), '--', label="CZT (standard)")
axes[1].set(title="CZT vs FFT (full spectrum)", xlabel="k")
axes[1].legend(fontsize=7)

axes[2].plot(freqs_zoom, np.abs(X_zoom))
axes[2].set(title=f"CZT Zoom [{f1}–{f2}] normalized freq", xlabel="Normalized Frequency")

plt.tight_layout()
plt.show()
