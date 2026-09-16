
import matplotlib.pyplot as plt
import numpy as np

LAMBDA=0.3

data=np.loadtxt("decay_observed.csv",delimiter=",",skiprows=1)
t=data[:,0]
observed=data[:,1]

N0=observed[0]
analytical=N0*np.exp(-LAMBDA*t)

fig, (ax1,ax2)=plt.subplots(1,2,sharex=True,sharey=True,figsize=(10,4))


ax1.scatter(t,observed,color="tab:blue",label="Observed",zorder=3)
ax1.set_title("Observed Data")
ax1.set_xlabel("Time ($t$)")
ax1.set_ylabel("Counts ($N$)")
ax1.grid(True,linestyle="--",alpha=0.5)
ax1.legend()


ax2.plot(t,analytical,color="tab:red",label=r"Analytical ($N_0 e^{-\lambda t}$)",linewidth=2)
ax2.set_title("Analytical Law ($\lambda = 0.3$)")
ax2.set_xlabel("Time ($t$)")
ax2.grid(True,linestyle="--",alpha=0.5)
ax2.legend()


plt.tight_layout()


plt.savefig("figure.png", dpi=300)
print("Figure saved successfully as figure.png!")