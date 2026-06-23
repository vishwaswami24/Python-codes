"""Laplace Transform — continuous-time, s-domain (evaluated along imaginary axis = CFT)."""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 1000)
dt = t[1] - t[0]

# Example: x(t) = e^{-at} * u(t), analytical X(s) = 1/(s+a)
a = 2.0
x = np.exp(-a * t)

sigma = np.linspace(-1, 5, 200)   # real part of s
omega = np.linspace(-20, 20, 200) # imag part of s

# Evaluate |X(s)| on the imaginary axis (s = jω)
X_jw = np.array([np.sum(x * np.exp(-1j * w * t)) * dt for w in omega])

# Evaluate magnitude on 2D s-plane (σ + jω grid)
S_sigma, S_omega = np.meshgrid(sigma, omega)
S = S_sigma + 1j * S_omega
X_s = np.array([
    [np.sum(x * np.exp(-s * t)) * dt for s in row]
    for row in S
])

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

axes[0].plot(t, x)
axes[0].set(title="Signal x(t) = e^{-at}", xlabel="t")

axes[1].plot(omega, np.abs(X_jw))
axes[1].set(title="|X(jω)| — on imaginary axis", xlabel="ω")

axes[2].contourf(S_sigma, S_omega, np.log1p(np.abs(X_s)), levels=50, cmap="inferno")
axes[2].set(title="|X(s)| — s-plane (log scale)", xlabel="σ", ylabel="jω")
axes[2].axvline(0, color='w', linewidth=0.5)

plt.tight_layout()
plt.show()
