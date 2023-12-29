import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt

# Function to check whether a dart hits within the unit circle
def is_hit(P, Q):
    return (P**2 + Q**2) <= 1

# Function to simulate a dart throw and calculate the probability of hitting within the circle
def simulate_dart_throw(num_darts):
    hits = 0
    for _ in range(num_darts):
        P = random.uniform(-1, 1)
        Q = random.uniform(-1, 1)
        if is_hit(P, Q):
            hits += 1
    prob_hit_circle = hits / num_darts
    return prob_hit_circle

# Accepting multiple values of N
n_values = [int(n) for n in input("Enter multiple values of N separated by commas: ").split(',')]

# Running the dart throw simulation for each value of N
results = []

for num_darts in n_values:
    prob_hit_circle = simulate_dart_throw(num_darts)
    estimate_value_pi = 4 * prob_hit_circle
    results.append({'N': num_darts, 'Pi Estimate': estimate_value_pi, 'True Pi': np.pi})

# Creating a DataFrame from the results
df = pd.DataFrame(results)

# Saving the DataFrame to an Excel file
df.to_excel('pi_estimation_results.xlsx', index=False)

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(df['N'], df['Pi Estimate'], label='Estimated Pi')
plt.axhline(np.pi, color='red', linestyle='--', label='True Pi')
plt.xlabel('Number of Darts (N)')
plt.ylabel('Estimated Pi Value')
plt.title('Estimation of Pi with Increasing Number of Darts')
plt.legend()
plt.grid(True)
plt.show()

# Displaying the DataFrame
print("Results have been saved to 'pi_estimation_results.xlsx'")
print(df)
