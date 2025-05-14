import numpy as np
import random as r
import math

print(f"{'-'*29}Output{'-'*29}")

# Objective function: minimize f(x) = x^2
def objective_function(x):
    return x ** 2

# Initialize parameters
x = r.uniform(-5, 5)     # Initial random value of x between -5 and 5
alpha = 0.95             # Cooling rate
temp = 100               # Initial temperature
num_steps = 10           # Number of iterations

energy = objective_function(x)  # Current energy
best_energy = energy            # Best (minimum) energy found
best_x = x                      # Best solution found

# Simulated Annealing main loop
for iter in range(num_steps):
    temperature = temp * math.pow(alpha, iter)

    # Generate a neighboring solution
    neighbour_x = x + np.random.uniform(-1, 1)
    neighbour_energy = objective_function(neighbour_x)

    delta_E = neighbour_energy - energy

    # Accept the new solution if it's better or with some probability if it's worse
    if delta_E < 0 or math.exp(-delta_E / temperature) > r.random():
        x = neighbour_x
        energy = neighbour_energy

    # Update the best solution
    if energy < best_energy:
        best_energy = energy
        best_x = x

    # Print progress
    print(f"Iteration {iter + 1}: x = {x:.4f}, Energy = {energy:.4f}, Temperature = {temperature:.4f}")

# Final result
print("\nOptimal solution: x =", round(best_x, 4))
print("Minimum energy:", round(best_energy, 4))