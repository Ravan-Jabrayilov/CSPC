import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("titration.csv", delimiter=",", skiprows=1)

V = data[:, 0]
pH = data[:, 1]

# Calculate dpH/dV
slope = np.gradient(pH, V)

# Equivalence point = maximum slope
equivalence_index = np.argmax(slope)
equivalence_volume = V[equivalence_index]

print("Equivalence point =", equivalence_volume, "mL")


fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(V, pH)
axes[0].set_xlabel("Volume of base (mL)")
axes[0].set_ylabel("pH")
axes[0].set_title("Titration curve")

axes[1].plot(V, slope)
axes[1].axvline(equivalence_volume, color="red", linestyle="--",
                label=f"Equivalence = {equivalence_volume:.1f} mL")
axes[1].set_xlabel("Volume of base (mL)")
axes[1].set_ylabel("dpH/dV")
axes[1].set_title("Titration curve slope")
axes[1].legend()

plt.tight_layout()
plt.savefig("titration.png")
plt.show()
