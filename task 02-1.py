import itertools

def count_ways_to_make_sum(target_sum, num_dice, num_sides):
    ways_to_make_sum = 0
    total_outcomes = 0

    # Generate all possible outcomes
    outcomes = itertools.product(range(1, num_sides + 1), repeat=num_dice)

    for outcome in outcomes:
        total_outcomes += 1
        if sum(outcome) == target_sum:
            ways_to_make_sum += 1

    return ways_to_make_sum, total_outcomes

# Parameters
target_sum = 32
num_dice = 10
num_sides = 6

# Calculate
ways_to_make_sum, total_outcomes = count_ways_to_make_sum(target_sum, num_dice, num_sides)
exact_probability = ways_to_make_sum / total_outcomes

# Output
print(f"Number of ways to make {target_sum} with {num_dice} dice: {ways_to_make_sum}")
print(f"Total possible outcomes with {num_dice} dice: {total_outcomes}")
print(f"Exact probability: {exact_probability}")
