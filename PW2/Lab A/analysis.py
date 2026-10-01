import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

data = np.loadtxt('freefall.csv', delimiter=',', skiprows=1)
t = data[:, 0]
y = data[:, 1]

v = np.gradient(y, t)
a = np.gradient(v, t)

v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]

mean_a = np.mean(a)
std_a = a.std()
max_diff = np.max(np.abs(y - y_rec))

print(f"Mean acceleration: {mean_a:.4f} m/s^2")
print(f"Standard deviation of acceleration: {std_a:.4f} m/s^2")
print(f"Largest position difference: {max_diff:.4f} m")

fig, axes = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

axes[0].plot(t, y, label='Original Position', color='blue', alpha=0.7)
axes[0].plot(t, y_rec, label='Recovered Position', color='orange', linestyle='--', alpha=0.9)
axes[0].set_ylabel('Position (m)')
axes[0].legend(loc='lower left')
axes[0].grid(True)
axes[0].set_title('Free Fall Motion Analysis: Differentiation vs. Integration')

axes[1].plot(t, v, label='Velocity', color='green')
axes[1].set_ylabel('Velocity (m/s)')
axes[1].grid(True)

axes[2].plot(t, a, label='Measured Acceleration', color='red', alpha=0.5)
axes[2].axhline(-9.81, color='black', linestyle='--', label='Expected (-9.81 m/s²)')
axes[2].set_ylabel('Acceleration (m/s²)')
axes[2].set_xlabel('Time (s)')
axes[2].legend(loc='upper right')
axes[2].grid(True)

plt.tight_layout()
plt.savefig('motion.png', dpi=300)
plt.show()