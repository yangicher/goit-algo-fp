import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def simulate_dice_rolls(num_simulations):
    rolls = np.random.randint(1, 7, size=(num_simulations, 2))
    sums = np.sum(rolls, axis=1)

    sum_frequencies = Counter(sums)

    probabilities = {total: (count / num_simulations) * 100 for total, count in sorted(sum_frequencies.items())}
    return probabilities

def plot_probability_distribution(probabilities):
    sums = list(probabilities.keys())
    probabilities_values = list(probabilities.values())

    plt.figure(figsize=(10, 6))
    plt.bar(sums, probabilities_values, color="skyblue", edgecolor="black")
    plt.xlabel("Sum of Dice Rolls")
    plt.ylabel("Probability (%)")
    plt.title("Probability Distribution of Dice Roll Sums")
    plt.xticks(sums)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

def main():
    num_simulations = int(input("Enter the number of simulations: "))
    probabilities = simulate_dice_rolls(num_simulations)

    print("\nProbability Distribution of Dice Rolls:")
    for total, probability in probabilities.items():
        print(f"Sum {total}: {probability:.2f}%")

    plot_probability_distribution(probabilities)

if __name__ == "__main__":
    main()
