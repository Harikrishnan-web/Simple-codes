# Bayes' Theorem Implementation

# Input values
P_H = 0.005  # Prior: P(Disease)
P_not_H = 1 - P_H  # Complement: P(No Disease)
P_E_given_H = 0.98  # Likelihood: P(Positive Test | Disease)
P_E_given_not_H = 0.02  # False Positive Rate: P(Positive Test | No Disease)

# Total probability of evidence (i.e., positive test)
P_E = (P_E_given_H * P_H) + (P_E_given_not_H * P_not_H)

# Apply Bayes' Theorem to get the posterior: P(Disease | Positive Test)
P_H_given_E = (P_E_given_H * P_H) / P_E

# Output result
print("Probability of having the disease given a positive test result:")
print(f"P(Disease | Positive Test) = {P_H_given_E:.4f} or {P_H_given_E * 100:.2f}%")
