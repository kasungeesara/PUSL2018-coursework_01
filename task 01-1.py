import random
import math

def throw_dart():
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    distance = math.sqrt(x**2 + y**2)
    return distance <= 1

def simulate_darts(num_throws):
    hits = 0
    for _ in range(num_throws):
        if throw_dart():
            hits += 1
    return hits / num_throws

#Simulate throws:
hits=int(input("enter the throws: "))
print(f"number of throws:{hits}")
probability_of_hitting = simulate_darts(hits)

print(f"Probability of hitting: {probability_of_hitting}")
print(f"value of pi: {math.pi}")

# Estimate pi using the simulation
estimated_pi = probability_of_hitting * 4
print(f"Estimated value of pi: {estimated_pi}")