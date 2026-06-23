"""Z-Transform — discrete-time, z-domain."""
import numpy as np
import matplotlib.pyplot as plt

# Example: x[n] = a^n * u[n], analytical X(z) = z/(z-a)
a = 0.7
N = 30
n = np.arange(N)
x = a ** n

# Evaluate on unit circle z = e^{jω}
omega = np.linspace(-np.pi, np.pi, 512)
X_unit = np.array([np.sum(x * np.exp(-1j * w * n)) for w in omega])

# Evaluate |X(z)| on 2D z-plane grid
re = np.linspace(-2, 2, 300)
im = np.linspace(-2, 2, 300)
RE, IM = np.meshgrid(re, im)
Z = RE + 1j * IM
X_z = np.array([
    [np.sum(x * z_val ** -np.arange(N)) for z_val in row]
    for row in Z
])

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

axes[0].stem(n, x)
axes[0].set(title="Signal x[n] = a^n u[n]", xlabel="n")

axes[1].plot(omega, np.abs(X_unit))
axes[1].set(title="|X(e^{jω})| — unit circle", xlabel="ω (rad/sample)")
axes[1].set_xticks([-np.pi, 0, np.pi])
axes[1].set_xticklabels(['-π', '0', 'π'])

axes[2].contourf(RE, IM, np.log1p(np.abs(X_z)), levels=50, cmap="plasma")
theta = np.linspace(0, 2 * np.pi, 300)
axes[2].plot(np.cos(theta), np.sin(theta), 'w--', linewidth=0.8, label="unit circle")
axes[2].plot(a, 0, 'rx', markersize=8, label=f"pole @ {a}")
axes[2].set(title="|X(z)| — z-plane (log scale)", xlabel="Re", ylabel="Im")
axes[2].legend(fontsize=7)

plt.tight_layout()
plt.show()
