import math
import random
def cost_function(x):
    return x * x
def neighbor(x):
    delta = (random.random() - 0.5) * 2.0
    return x + delta
def simulated_annealing(start, temp, cooling_rate, max_iter):
    current = start
    best = current
    current_cost = cost_function(current)
    best_cost = current_cost
    for i in range(max_iter):
        next_x = neighbor(current)
        next_cost = cost_function(next_x)
        if next_cost < current_cost or \
           math.exp((current_cost - next_cost) / temp) > random.random():
            current = next_x
            current_cost = next_cost
            if current_cost < best_cost:
                best = current
                best_cost = current_cost
        temp *= cooling_rate
        if temp < 1e-8:
            break
    return best
if __name__ == "__main__":
    random.seed()
    start = 10.0
    temp = 1000.0
    cooling_rate = 0.99
    max_iter = 10000

    result = simulated_annealing(start, temp, cooling_rate, max_iter)
    print(f"Minimum found at x = {result}, f(x) = {cost_function(result)}")