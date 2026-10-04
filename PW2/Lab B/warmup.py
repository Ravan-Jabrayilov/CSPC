import numpy as np
from scipy.optimize import minimize, newton

# --- Part 2A Functions ---
def f(x):
    return (x - 3)**2 + 1

def f_prime(x):
    return 2 * (x - 3)

def f_double_prime(x):
    return 2

# --- Part 2B Functions ---
def g(x):
    return x**4 - 3*x**2 + x + 5

def g_prime(x):
    return 4*x**3 - 6*x + 1

def g_double_prime(x):
    return 12*x**2 - 6

def run_methods(x0, name):
    print(f"\n--- Results starting from x0 = {x0} ({name}) ---")
    
    # 1. Gradient Descent by hand
    x = x0
    learning_rate = 0.05
    for _ in range(100):
        x = x - learning_rate * g_prime(x)
    print(f"1. Gradient Descent: x = {x:.6f}, g(x) = {g(x):.6f}") 

    # 2. Newton's Method on g'(x) = 0
    try:
        x_newton = newton(g_prime, x0=x0, fprime=g_double_prime)
        g2 = g_double_prime(x_newton)
        status = "Minimum (g'' > 0)" if g2 > 0 else "Maximum (g'' < 0)"
        print(f"2. Newton's Method:  x = {x_newton:.6f}, g''(x) = {g2:.2f} -> {status}")
    except RuntimeError as e:
        print(f"2. Newton's Method:  Failed to converge ({e})")

    # 3. SLSQP via scipy.optimize.minimize
    res = minimize(g, x0=[x0], method="SLSQP")
    print(f"3. SLSQP (Minimize): x = {res.x[0]:.6f}, g(x) = {res.fun:.6f}")

def main():
    # Part 2A execution
    print("--- Part 2A: Easy Convex Function ---")
    x0 = 0.0
    x_newton = newton(f_prime, x0=x0, fprime=f_double_prime)
    res_slsqp = minimize(f, x0=[x0], method="SLSQP")
    print(f"Newton: {x_newton:.4f} | SLSQP: {res_slsqp.x[0]:.4f}")

    # Part 2B execution
    run_methods(0.0, "Near center/maximum region")
    run_methods(2.0, "In the right-hand basin")

if __name__ == "__main__":
    main(
)