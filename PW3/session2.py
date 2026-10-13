import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

df_heart = pd.read_csv("heart.csv")

print("=== SESSION 2: HEART DATA ANALYSIS ===")

group_disease = df_heart[df_heart["target"] == 1]["thalach"]
group_healthy = df_heart[df_heart["target"] == 0]["thalach"]

mean_disease, sem_disease = group_disease.mean(), stats.sem(group_disease)
mean_healthy, sem_healthy = group_healthy.mean(), stats.sem(group_healthy)

print(f"Healthy Thalach: Mean = {mean_healthy:.2f} ± {sem_healthy:.2f} (SEM)")
print(f"Disease Thalach: Mean = {mean_disease:.2f} ± {sem_disease:.2f} (SEM)")

t_stat, p_val = stats.ttest_ind(group_disease, group_healthy, equal_var=False)
print(f"Welch's t-test: t = {t_stat:.4f}, p = {p_val:.4e}")

plt.figure(figsize=(6, 5))
groups = ['Healthy (0)', 'Disease (1)']
means = [mean_healthy, mean_disease]
sems = [sem_healthy, sem_disease]
plt.bar(groups, means, yerr=sems, capsize=5, color=['skyblue', 'salmon'], alpha=0.8)
plt.ylabel("Maximum Heart Rate (thalach)")
plt.title("Max Heart Rate by Heart Disease Status (with SEM)")
plt.savefig("thalach_comparison.png")
plt.close()
print("Saved thalach comparison plot to thalach_comparison.png")

r_val, p_corr = stats.pearsonr(df_heart["age"], df_heart["thalach"])
print(f"\nPearson correlation (Age vs Thalach): r = {r_val:.4f}, p = {p_corr:.4e}")

plt.figure(figsize=(6, 5))
plt.scatter(df_heart["age"], df_heart["thalach"], alpha=0.6, edgecolors='w', label='Patients')

m, b = np.polyfit(df_heart["age"], df_heart["thalach"], 1)
plt.plot(df_heart["age"], m * df_heart["age"] + b, color='red', linewidth=2, label=f'Trend line (r = {r_val:.2f})')

plt.xlabel("Age")
plt.ylabel("Maximum Heart Rate (thalach)")
plt.title("Age vs. Maximum Heart Rate")
plt.legend()
plt.savefig("age_vs_thalach.png")
plt.close()
print("Saved age vs thalach scatter plot with trend line to age_vs_thalach.png")


print("\n=== CHEMICAL-EXPOSURE MYSTERY ANALYSIS ===")
df_chem = pd.read_csv("chemicals_cancer.csv")

r_benz, p_benz = stats.pearsonr(df_chem["benzene"], df_chem["malignancy"])
r_cadm, p_cadm = stats.pearsonr(df_chem["cadmium"], df_chem["malignancy"])
print(f"Naive Benzene vs Malignancy: r = {r_benz:.4f} (p = {p_benz:.4e})")
print(f"Naive Cadmium vs Malignancy: r = {r_cadm:.4f} (p = {p_cadm:.4e})")

print("\n--- Confounding Analysis (Pollution Index) ---")
median_poll = df_chem["pollution index"].median()
low_poll = df_chem[df_chem["pollution index"] <= median_poll]
high_poll = df_chem[df_chem["pollution index"] > median_poll]

print("[Low Pollution Stratum]")
print("  Benzene vs Malignancy r:", stats.pearsonr(low_poll["benzene"], low_poll["malignancy"])[0])
print("  Cadmium vs Malignancy r:", stats.pearsonr(low_poll["cadmium"], low_poll["malignancy"])[0])

print("[High Pollution Stratum]")
print("  Benzene vs Malignancy r:", stats.pearsonr(high_poll["benzene"], high_poll["malignancy"])[0])
print("  Cadmium vs Malignancy r:", stats.pearsonr(high_poll["cadmium"], high_poll["malignancy"])[0])


print("\n=== BONUS: CATEGORICAL BALANCE ===")
target_props = df_heart["target"].value_counts(normalize=True)
print("Target Proportions:\n", target_props)