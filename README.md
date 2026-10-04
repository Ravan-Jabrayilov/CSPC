# My Lab Repository

# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.
## Setup
Create the environment for a given lab:
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc
---
## PW1 - Lab A: Reproducible Foundations

**Pre-Questions:**

**Which pytest tool checks that an error is raised?**

it is pytest.raises(). you can check what you expect and use match 

**Which pytest tool compares floating-point values with a tolerance?**

it is pytest.approx(). it is very useful because if you want to check some calculation and your numbers are float, use approx, because if you dont use it, for example, 0.1+0.2=0.3 will be wrong.

**what i built?**

i built conda environment file, CSPC repository with git, atom decay simulation with the help of speed.py.

**speed comparison:**

Pure-Python loop: 1.9490 seconds
NumPy version:    0.0002 seconds
NumPy is 11421.14 times faster

**Tests?**

all tests are passed

**Conclusion:**

From the answer of speed.py, we saw how fast Numpy is instead of pure python loop, that shows when we are working on large simulations, Numpy is much more useful than original, and also there was no problems with atom decay tests, all tests are passed.


## PW1 --- Lab B

The observed data showed an exponential decrease over time. The observed
points are almost same with the analytical decay law
N(t)=N0e^{-0.3t}, although there were some differences between the measured
values and the analytical curve.

The Snakemake pipeline automates the generation of the figure by using
`decay_observed.csv` as input, running `plot.py`, and producing `figure.png` as
the output. It also avoids from repeating the step when the input files have not changed.

## PW2 --- Lab A

**Mean Acceleration Measured:** 
approximately -9.81 (confirming free fall).

**Why Acceleration is Noisy:** 
finding the derivative makes small measurement errors much bigger, so doing it twice turns tiny mistakes into huge jumps in the acceleration.

**What Integrating Back Showed:** 
integration acts like a running sum where random noise errors cancel each other out, successfully cleaning up the noise and recovering the original position within about 1 metre.


# CSPC - PW2 Lab B: Optimization

## Part 2A: Easy Function f(x) = (x-3)^2 + 1
starting from x_0=0, all three methods (gradient descent, Newton's method, SLSQP) successfully reach the global minimum at x=3.

## Part 2B: Harder Landscape g(x)=x^4-3x^2+x+5

* **Do the methods agree?** no from x_0=0 (they end up in different places). yes from x_0 = 2 (all methods find the right-side minimum at x approximately 1.140).
* **Did Newton land on a minimum or maximum?** 
* From x_0 = 0, Newton landed at x approximately 0.171 where g<0, which is a **maximum**. Newton only looks for slope=0, not a minimum.
* From x_0 = 2, Newton landed on a **minimum** (g>0).
* **How did the starting point change the result?** the starting point changes everything on a hard landscape because different spots trap the methods in different valleys or hills.

## Part 3: Fit a Reaction Rate (`kinetics.py`)

find the rate constant k for a first-order decay C(t)=C_0e^{-kt} by minimizing the squared error between noisy data and the model.
using `SLSQP`, the fitted rate constant is k approximately 0.25. the generated plot (`kinetics.png`) shows the fitted curve passing closely through the measured data points.

## Part 4 — Chemical Equilibrium

for H₂ + I₂ ⇌ 2HI, i found the equilibrium extent x using Newton’s method and SLSQP minimisation. both methods gave approximately x=0.66, giving H2=0.34 mol, I2=0.34 mol, and HI=1.33 mol.

## Part 5 — Titration Equivalence Point

i calculated the slope of the pH curve using np.gradient() and used np.argmax() to find its maximum. The equivalence point was approximately 50 mL, where the pH changes most rapidly.

..............

##Summary:

kinetics:

for the simple function, all three methods—gradient descent, Newton's method, and SLSQP—agreed and found the minimum at x≈3.

for the harder function, the methods did not always agree. newton's method finds a stationary point rather than necessarily a minimum. Starting from x=0, it reached a maximum, while starting from x=2, it reached a minimum. this shows that the starting point and optimisation method can affect the result.


the fitted first-order rate constant was:

k≈0.25

equilibrium:

for H2+I2⇌2HI, both Newton's method and SLSQP gave:

    x=0.667

    H2=0.333 mol

    I2=0.333 mol

    HI=1.333 mol

titration:

the calculated titration equivalence point was approximately:

V=50 mL
