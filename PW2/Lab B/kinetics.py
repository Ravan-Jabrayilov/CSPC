import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# 1. Load data from kinetics.csv (assuming columns: time, concentration)
try:
    data = np.loadtxt('kinetics.csv', delimiter=',', skiprows=1)
except Exception:
    data = np.loadtxt('kinetics.csv', delimiter=',')

t = data[:, 0]
C_measured = data[:, 1]
C0 = C_measured[0]  # Set C0 to the first concentration value

# 2. Define the total error function (Sum of Squared Errors)
def error(k):
    k_val = k[0] if isinstance(k, (np.ndarray, list)) else k
    C_model = C0 * np.exp(-k_val * t)
    return np.sum((C_measured - C_model)**2)

# 3. Minimize error using SLSQP
res = minimize(error, x0=[0.5], method="SLSQP", bounds=[(0, 5)])
k_fitted = res.x[0]

print(f"Fitted rate constant k = {k_fitted:.4f}")

# 4. Plot the data and the fitted curve, save as kinetics.png
t_smooth = np.linspace(t.min(), t.max(), 200)
C_smooth = C0 * np.exp(-k_fitted * t_smooth)

plt.figure(figsize=(6, 4))
plt.scatter(t, C_measured, color='red', label='Measurements')
plt.plot(t_smooth, C_smooth, color='blue', label=f'Fitted Curve (k={k_fitted:.4f})')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.title('First-Order Kinetics Fitting')
plt.savefig('kinetics.png', dpi=300, bbox_inches='tight')
plt.show()