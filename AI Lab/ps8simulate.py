import random
disease_rate = 0.01         
true_positive_rate = 0.95     
false_positive_rate = 0.05    
patients = 10000

positive_total = 0
disease_and_positive = 0

# Simulation
for _ in range(patients):
    has_disease = random.random() < disease_rate
    if has_disease:
        test_positive = random.random() < true_positive_rate
    else:
        test_positive = random.random() < false_positive_rate

    if test_positive:
        positive_total += 1
        if has_disease:
            disease_and_positive += 1

# Bayes estimate
if positive_total > 0:
    prob_disease_given_positive = disease_and_positive / positive_total
    print(f"Estimated P(Disease | Test Positive): {prob_disease_given_positive:.4f}")
else:
    print("No positive tests recorded.")
