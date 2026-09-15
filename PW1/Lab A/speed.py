import time
from decay import simulate, simulate_loop

N0 = 200000
lam = 0.4

# Time the pure-Python version
start = time.perf_counter()
simulate_loop(N0, lam)
loop_time = time.perf_counter() - start

# Time the NumPy version
start = time.perf_counter()
simulate(N0, lam)
numpy_time = time.perf_counter() - start

# Calculate speedup
speedup = loop_time / numpy_time

print(f"Pure-Python loop: {loop_time:.4f} seconds")
print(f"NumPy version:    {numpy_time:.4f} seconds")
print(f"NumPy is {speedup:.2f} times faster")
