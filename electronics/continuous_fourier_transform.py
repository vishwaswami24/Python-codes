"""Continuous Fourier Transform (CFT) — continuous, aperiodic signals."""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 5, 1000)
dt = t[1] - t[0]

# Example: rectangular pulse
x = np.where(np.abs(t) <= 1, 1.0, 0.0)

freqs = np.linspace(-10, 10, 500)
X = np.array([np.sum(x * np.exp(-1j * 2 * np.pi * f * t)) * dt for f in freqs])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(t, x)
ax1.set(title="Signal x(t)", xlabel="t")

ax2.plot(freqs, np.abs(X))
ax2.set(title="|X(f)| — CFT Magnitude", xlabel="Frequency (Hz)")

plt.tight_layout()
plt.show()
