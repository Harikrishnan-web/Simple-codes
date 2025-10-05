# Forward Chaining Inference System

# Knowledge base of rules
rules = [
    {"if": ["A", "B"], "then": "C"},
    {"if": ["C"], "then": "D"},
    {"if": ["D", "E"], "then": "F"},
    {"if": ["F"], "then": "G"}
]

# Initial known facts
facts = {"A", "B", "E"}

# Goal to be inferred
goal = "G"

# Forward Chaining Function
def forward_chaining(rules, facts, goal):
    inferred = set()
    while True:
        new_inference = False
        for rule in rules:
            # Skip if the conclusion is already known
            if rule["then"] in facts:
                continue

            # Check if all conditions are satisfied
            if all(condition in facts for condition in rule["if"]):
                conclusion = rule["then"]
                facts.add(conclusion)
                inferred.add(conclusion)
                new_inference = True
                print(f"Inferred: {conclusion} from {rule['if']}")
                if conclusion == goal:
                    return True

        if not new_inference:
            break

    return goal in facts

# Run the forward chaining algorithm
result = forward_chaining(rules, facts, goal)

# Display final results
print("\nFinal Facts Inferred:", facts)
print("Goal Reached:", result)
