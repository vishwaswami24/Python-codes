"""Wavelet Transform — CWT and DWT (multi-resolution time-scale analysis)."""
import numpy as np
import matplotlib.pyplot as plt
import pywt

fs = 1000
t  = np.linspace(0, 1, fs, endpoint=False)

# Signal: two bursts at different frequencies
x = np.zeros(fs)
x[100:200] += np.sin(2 * np.pi * 50  * t[100:200])
x[500:700] += np.sin(2 * np.pi * 200 * t[500:700])

# --- CWT ---
scales = np.arange(1, 128)
wavelet = 'cmor1.5-1.0'
coeffs_cwt, freqs_cwt = pywt.cwt(x, scales, wavelet, sampling_period=1/fs)

# --- DWT (multi-level decomposition) ---
wavelet_dwt = 'db4'
level = 5
coeffs_dwt = pywt.wavedec(x, wavelet_dwt, level=level)

fig, axes = plt.subplots(3, 1, figsize=(11, 9))

axes[0].plot(t, x)
axes[0].set(title="Signal x(t)", xlabel="Time (s)")

axes[1].contourf(t, freqs_cwt, np.abs(coeffs_cwt), levels=50, cmap='inferno')
axes[1].set(title="CWT Scalogram", xlabel="Time (s)", ylabel="Frequency (Hz)", ylim=(0, 300))

for i, c in enumerate(coeffs_dwt):
    label = "Approx" if i == 0 else f"Detail {i}"
    axes[2].plot(np.linspace(0, 1, len(c)), c + i * 2, label=label)
axes[2].set(title="DWT Decomposition (db4, level 5)", xlabel="Normalized time")
axes[2].legend(fontsize=7, loc='upper right')

plt.tight_layout()
plt.show()
