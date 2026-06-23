"""Discrete Fourier Transform (DFT) — discrete, aperiodic (finite-length) signal."""
import numpy as np
import matplotlib.pyplot as plt

# Example: finite rectangular pulse
N = 64
x = np.zeros(N)
x[10:20] = 1.0

X = np.fft.fft(x)
freqs = np.fft.fftfreq(N)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.stem(x)
ax1.set(title="Signal x[n]", xlabel="n")

ax2.stem(np.fft.fftshift(freqs), np.fft.fftshift(np.abs(X)))
ax2.set(title="|X[k]| — DFT Magnitude", xlabel="Normalized Frequency")

plt.tight_layout()
plt.show()
