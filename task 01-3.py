import numpy as np
import random
import pandas as pd

# Checking whether the dart hits within the circle
def is_hit(P, Q):
    return (P**2 + Q**2) <= 1

# Simulating the dart throw
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

# Running the dart throw simulation for each value of N, each experiment 10 times
results = []

for num_darts in n_values:
    for _ in range(10):  # Run each experiment 10 times
        prob_hit_circle = simulate_dart_throw(num_darts)
        estimate_value_pi = 4 * prob_hit_circle
        results.append({'N': num_darts, 'Pi Estimate': estimate_value_pi, 'True Pi': np.pi})

# Creating a DataFrame from the results
df = pd.DataFrame(results)

# Calculating mean and mode for each N
df['Mean Pi Estimate'] = df.groupby('N')['Pi Estimate'].transform('mean')
df['Mode Pi Estimate'] = df.groupby('N')['Pi Estimate'].transform(lambda x: x.mode().iloc[0])

# Saving the DataFrame to an Excel file with a new name and sheet name
df.to_excel('excel_results.xlsx', index=False, sheet_name='Sheet1')

# Displaying the DataFrame
print(f"Results have been saved to 'excel_results.xlsx'")
print(df)
