import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_simulations):
    sum_frequencies = {total: 0 for total in range(2, 13)}

    for _ in range(num_simulations):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total_sum = die1 + die2
        sum_frequencies[total_sum] += 1

    probabilities = {total: (count / num_simulations) * 100 for total, count in sum_frequencies.items()}
    return probabilities

def plot_probability_distribution(probabilities):
    sums = list(probabilities.keys())
    probabilities_values = list(probabilities.values())

    plt.figure(figsize=(10, 6))
    plt.bar(sums, probabilities_values, color="skyblue")
    plt.xlabel("Sum of Dice Rolls")
    plt.ylabel("Probability (%)")
    plt.title("Probability Distribution of Dice Roll Sums")
    plt.xticks(sums)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

def main():
    num_simulations = 100000
    probabilities = simulate_dice_rolls(num_simulations)

    print("Probability Distribution of Dice Rolls:")
    for total, probability in probabilities.items():
        print(f"Sum {total}: {probability:.2f}%")

    plot_probability_distribution(probabilities)

if __name__ == "__main__":
    main()
