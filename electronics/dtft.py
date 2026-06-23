"""Discrete-Time Fourier Transform (DTFT) — discrete-time, aperiodic signal."""
import numpy as np
import matplotlib.pyplot as plt

# Example: decaying exponential x[n] = a^n * u[n]
a = 0.7
N = 30
n = np.arange(N)
x = a ** n   # causal signal

# Evaluate DTFT at many frequencies (continuous spectrum over [-π, π])
omega = np.linspace(-np.pi, np.pi, 1000)
X = np.array([np.sum(x * np.exp(-1j * w * n)) for w in omega])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.stem(n, x)
ax1.set(title="Signal x[n]", xlabel="n")

ax2.plot(omega, np.abs(X))
ax2.set(title="|X(e^jω)| — DTFT Magnitude", xlabel="ω (rad/sample)")
ax2.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
ax2.set_xticklabels(['-π', '-π/2', '0', 'π/2', 'π'])

plt.tight_layout()
plt.show()
