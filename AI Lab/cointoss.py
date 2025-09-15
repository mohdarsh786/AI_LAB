import random
import matplotlib.pyplot as plt  # Added for plotting
def tosses(n, p):
    result = {"H": 0, "T": 0}
    for _ in range(n):
        side = "H" if random.random() < p else "T"
        result[side] += 1
    return result

def probs(result, n):
    return {
        "P(Head)": result["H"] / n,
        "P(Tail)": result["T"] / n
    }

n = 500
fair = tosses(n, p=0.5)
fair_p = probs(fair, n)
print(f"Counts: {fair}")
print(f"Experimental Probabilities: {fair_p}")
print("Theoretical Probabilities: {'P(Head)': 0.5, 'P(Tail)': 0.5}\n")

print("biased coin toss")
biased = tosses(n, p=0.7)
biased_p = probs(biased, n)
print(f"Counts: {biased}")
print(f"Experimental Probabilities: {biased_p}")
print("Theoretical Probabilities: {'P(Head)': 0.7, 'P(Tail)': 0.3}")

# --- Matplotlib code for plotting ---
labels = ['Head', 'Tail']

# Fair coin
fair_exp = [fair_p["P(Head)"], fair_p["P(Tail)"]]
fair_theo = [0.5, 0.5]

# Biased coin
biased_exp = [biased_p["P(Head)"], biased_p["P(Tail)"]]
biased_theo = [0.7, 0.3]

x = range(len(labels))

fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# Fair coin plot
axs[0].bar(x, fair_exp, width=0.4, label='Experimental', align='center')
axs[0].bar([i + 0.4 for i in x], fair_theo, width=0.4, label='Theoretical', align='center')
axs[0].set_xticks([i + 0.2 for i in x])
axs[0].set_xticklabels(labels)
axs[0].set_ylim(0, 1)
axs[0].set_title('Fair Coin')
axs[0].legend()

# Biased coin plot
axs[1].bar(x, biased_exp, width=0.4, label='Experimental', align='center')
axs[1].bar([i + 0.4 for i in x], biased_theo, width=0.4, label='Theoretical', align='center')
axs[1].set_xticks([i + 0.2 for i in x])
axs[1].set_xticklabels(labels)
axs[1].set_ylim(0, 1)
axs[1].set_title('Biased Coin')
axs[1].legend()

plt.tight_layout()
plt.show()