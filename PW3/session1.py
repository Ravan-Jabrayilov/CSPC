import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

df_heart = pd.read_csv("heart.csv")
print(f"Dataset Shape: {df_heart.shape}")
print(df_heart.head())

continuous_cols = ["age", "chol", "trestbps", "thalach"]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.flatten()
for i, col in enumerate(continuous_cols):
    axes[i].hist(df_heart[col].dropna(), bins=20, edgecolor='black', alpha=0.7)
    axes[i].set_title(f"Distribution of {col}")
    axes[i].set_xlabel(col)
    axes[i].set_ylabel("Frequency")
plt.tight_layout()
plt.savefig("heart_distributions.png")
plt.close()
print("Saved distribution plot to heart_distributions.png")

print("\n--- Normality Tests (Shapiro-Wilk) ---")
normality_results = {}
for col in continuous_cols:
    stat, p_value = stats.shapiro(df_heart[col].dropna())
    is_normal = p_value > 0.05
    normality_results[col] = (stat, p_value, is_normal)
    print(f"{col}: W = {stat:.4f}, p-value = {p_value:.4e} -> Normal? {is_normal}")

