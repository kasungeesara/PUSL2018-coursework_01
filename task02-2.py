import random


def simulate_dice_throws(num_simulations, num_dice, target_sum):
    successful_outcomes = 0
    successful_dice_results = None  # Store successful dice results

    for _ in range(num_simulations):
        dice_results = [random.randint(1, 6) for _ in range(num_dice)]
        if sum(dice_results) == target_sum:
            successful_outcomes += 1
            successful_dice_results = dice_results

    probability_simulation = successful_outcomes / num_simulations
    return probability_simulation, successful_dice_results


num_simulations = 500
num_dice_simulation = 10
target_sum_simulation = 32

probability_simulation, successful_dice_results = simulate_dice_throws(num_simulations, num_dice_simulation,
                                                                       target_sum_simulation)

print(f"Simulated probability: {probability_simulation:.6f}")

#if successful_dice_results:
print(f"Random numbers for 10 dice throws: {successful_dice_results}")
