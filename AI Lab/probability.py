import random
total_rolls=1000
counts={i:0 for i in range(1,7)}
for _ in range(total_rolls):
    roll=random.randint(1,6)
    counts[roll]+=1
for outcome in range(1,7):
    experimental_prob=counts[outcome]/total_rolls
    theoretical_probe=1/6
    print(f"{outcome} | {experimental_prob:.3f} |")
