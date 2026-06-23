"""Hilbert Transform — analytic signal, envelope and instantaneous frequency."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert

fs = 1000
t  = np.linspace(0, 1, fs, endpoint=False)

# AM signal: carrier modulated by a low-frequency envelope
carrier = np.sin(2 * np.pi * 100 * t)
envelope_true = 0.5 + 0.5 * np.sin(2 * np.pi * 5 * t)
x = envelope_true * carrier

analytic  = hilbert(x)
envelope  = np.abs(analytic)
inst_phase = np.unwrap(np.angle(analytic))
inst_freq  = np.diff(inst_phase) / (2 * np.pi / fs)

fig, axes = plt.subplots(3, 1, figsize=(10, 8))

axes[0].plot(t, x, alpha=0.7, label="x(t)")
axes[0].plot(t, envelope, 'r', linewidth=1.5, label="Envelope")
axes[0].set(title="Signal & Envelope (Hilbert)", xlabel="Time (s)")
axes[0].legend()

axes[1].plot(t, inst_phase)
axes[1].set(title="Instantaneous Phase (rad)", xlabel="Time (s)")

axes[2].plot(t[1:], inst_freq)
axes[2].set(title="Instantaneous Frequency (Hz)", xlabel="Time (s)", ylim=(0, 200))

plt.tight_layout()
plt.show()
