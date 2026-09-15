# My Lab Repository

# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.
## Setup
Create the environment for a given lab:
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc
---
## PW1 - Lab A: Reproducible Foundations

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
