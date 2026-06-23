"""Hartley Transform — real-valued alternative to Fourier (continuous & discrete DHT)."""
import numpy as np
import matplotlib.pyplot as plt

# Discrete Hartley Transform (DHT) via FFT
def dht(x):
    X = np.fft.fft(x)
    return X.real - X.imag   # cas = cos + sin

def idht(H):
    return dht(H) / len(H)   # DHT is its own inverse (up to 1/N)

N = 64
n = np.arange(N)
x = np.sin(2 * np.pi * 5 * n / N) + 0.5 * np.cos(2 * np.pi * 15 * n / N)

H = dht(x)
x_rec = idht(H)

# Continuous Hartley Transform (numerical): H(f) = ∫ x(t) cas(2πft) dt
t_cont = np.linspace(-3, 3, 800)
dt = t_cont[1] - t_cont[0]
x_cont = np.exp(-t_cont**2)   # Gaussian (its own Hartley transform)

freqs = np.linspace(-5, 5, 400)
H_cont = np.array([
    np.sum(x_cont * (np.cos(2*np.pi*f*t_cont) + np.sin(2*np.pi*f*t_cont))) * dt
    for f in freqs
])

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].plot(t_cont, x_cont)
axes[0, 0].set(title="Continuous Signal (Gaussian)", xlabel="t")

axes[0, 1].plot(freqs, H_cont)
axes[0, 1].set(title="Continuous Hartley Transform H(f)", xlabel="f")

axes[1, 0].stem(n, x)
axes[1, 0].set(title="Discrete Signal x[n]", xlabel="n")

axes[1, 1].stem(n, H)
axes[1, 1].set(title="DHT Coefficients H[k]", xlabel="k")

plt.tight_layout()
plt.show()
