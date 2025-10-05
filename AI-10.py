# Backward Chaining Inference System

# Rules for inference
rules = {
    "C": ["A", "B"],
    "D": ["C"],
    "F": ["D", "E"],
    "G": ["F"]
}

# Known facts
facts = {"A", "B", "E"}

# Function to implement backward chaining
def backward_chaining(goal, facts, rules, visited=None):
    if visited is None:
        visited = set()

    if goal in facts:
        return True
    if goal in visited:
        return False  # Avoid infinite loops

    visited.add(goal)
    if goal not in rules:
        return False

    for premise in rules[goal]:
        if not backward_chaining(premise, facts, rules, visited):
            return False

    facts.add(goal)
    print(f"Inferred: {goal}")
    return True

# Goal to prove
goal = "G"

# Run the backward chaining
result = backward_chaining(goal, facts, rules)

# Display final result
print("\nFinal Facts:", facts)
print("Goal Reached:", result)
