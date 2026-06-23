"""Short-Time Fourier Transform (STFT) — time-frequency analysis."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft

fs = 1000          # sampling rate (Hz)
T  = 2.0           # duration (s)
t  = np.linspace(0, T, int(fs * T), endpoint=False)

# Chirp: frequency sweeps from 50 Hz to 300 Hz
x = np.sin(2 * np.pi * (50 + 125 * t) * t)

f, t_stft, Zxx = stft(x, fs=fs, window='hann', nperseg=128, noverlap=96)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
ax1.plot(t, x)
ax1.set(title="Chirp Signal x(t)", xlabel="Time (s)", ylabel="Amplitude")

ax2.pcolormesh(t_stft, f, np.abs(Zxx), shading='gouraud', cmap='inferno')
ax2.set(title="STFT Spectrogram", xlabel="Time (s)", ylabel="Frequency (Hz)", ylim=(0, 400))

plt.tight_layout()
plt.show()
