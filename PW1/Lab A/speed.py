import time
from decay import simulate, simulate_loop

N0=200000
lam=0.4

start=time.perf_counter()
simulate_loop(N0,lam)
loop-time=time.perf_counter()-start

start=time.perf_counter()
simulate(N0,lam)
numpy-time=time.perf_counter()-start

speedup=loop_time/numpy_time

print(f"Pure-Python loop: {loop-time:.4f} seconds")
print(f"NumPy version:    {numpy-time:.4f} seconds")
print(f"NumPy is {speedup:.2f} times faster")
