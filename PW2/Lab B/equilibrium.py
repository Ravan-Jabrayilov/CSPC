import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize


# ============================================================
# Part 4: Chemical equilibrium
#
# H2 + I2 <=> 2 HI
#
# Initial:
# n(H2) = 1 mol
# n(I2) = 1 mol
# n(HI) = 0 mol
#
# At extent x:
# n(H2) = 1 - x
# n(I2) = 1 - x
# n(HI) = 2x
#
# K = [HI]^2 / ([H2][I2])
#
# Therefore:
# (2x)^2 / ((1-x)(1-x)) - K = 0
# ============================================================

K = 16.0


def k_imbalance(x):
    """Equilibrium equation. Zero means equilibrium."""
    return (2 * x) ** 2 / ((1 - x) ** 2) - K


def k_imbalance_derivative(x):
    """
    Derivative of the equilibrium equation.

    f(x) = 4x^2/(1-x)^2 - K
    f'(x) = 8x/(1-x)^3
    """
    return 8 * x / (1 - x) ** 3


# ============================================================
# Method 1: Newton root-finding
# ============================================================

x_newton = newton(
    k_imbalance,
    x0=0.5,
    fprime=k_imbalance_derivative
)


# ============================================================
# Method 2: Minimise squared imbalance using SLSQP
# ============================================================

def squared_imbalance(x):
    x = float(np.asarray(x).ravel()[0])
    return k_imbalance(x) ** 2


result = minimize(
    squared_imbalance,
    x0=np.array([0.5]),
    method="SLSQP",
    bounds=[(0, 0.999999)]
)

x_slsqp = result.x[0]


# ============================================================
# Calculate equilibrium amounts
# ============================================================

n_H2 = 1 - x_newton
n_I2 = 1 - x_newton
n_HI = 2 * x_newton


print("=== Part 4: Chemical equilibrium ===")
print(f"K = {K}")
print(f"Newton equilibrium extent: x = {x_newton:.8f}")
print(f"SLSQP equilibrium extent:  x = {x_slsqp:.8f}")
print()
print("Equilibrium amounts using Newton:")
print(f"H2 = {n_H2:.8f} mol")
print(f"I2 = {n_I2:.8f} mol")
print(f"HI = {n_HI:.8f} mol")
print()
print(f"Newton imbalance = {k_imbalance(x_newton):.8e}")
print(f"SLSQP imbalance = {k_imbalance(x_slsqp):.8e}")


# ============================================================
# Plot concentrations/amounts versus reaction extent
# ============================================================

x_values = np.linspace(0, 0.95, 500)

H2_values = 1 - x_values
I2_values = 1 - x_values
HI_values = 2 * x_values

plt.figure(figsize=(8, 5))

plt.plot(
    x_values,
    H2_values,
    label="H₂",
    linewidth=2
)

plt.plot(
    x_values,
    I2_values,
    label="I₂",
    linewidth=2
)

plt.plot(
    x_values,
    HI_values,
    label="HI",
    linewidth=2
)

plt.axvline(
    x_newton,
    color="black",
    linestyle="--",
    label=f"Equilibrium x = {x_newton:.3f}"
)

plt.scatter(
    [x_newton],
    [n_HI],
    color="red",
    zorder=5
)

plt.xlabel("Reaction extent, x (mol)")
plt.ylabel("Amount (mol)")
plt.title("H₂ + I₂ ⇌ 2HI")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig("equilibrium.png", dpi=300)
plt.show()
