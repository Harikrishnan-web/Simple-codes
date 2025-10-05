import time
from itertools import product

def evaluate(formula, assignment):
    replaced_formula = formula
    for var, val in assignment.items():
        replaced_formula = replaced_formula.replace(var, str(val))
    try:
        return eval(replaced_formula)
    except Exception as e:
        print(f"\nError evaluating: {replaced_formula}")
        print(f"Reason: {e}")
        return False

def get_variables(formula):
    return sorted(set([c for c in formula if c.isalpha()]))

def model_checking(formula, max_seconds=5):
    variables = get_variables(formula)
    combinations = list(product([False, True], repeat=len(variables)))
    true_count = 0
    start_time = time.time()

    print(f"\nChecking formula: {formula}")
    for values in combinations:
        if time.time() - start_time > max_seconds:
            print(f"\n⏳ Time limit of {max_seconds} seconds reached.")
            break

        assignment = dict(zip(variables, values))
        result = evaluate(formula, assignment)
        if result:
            print(f"✔ Satisfying assignment: {assignment}")
            true_count += 1
        else:
            print(f"✘ Failed assignment: {assignment}")

    if true_count == len(combinations):
        print("\n□ Result: The formula is VALID (true in all models).")
    elif true_count > 0:
        print("\n□ Result: The formula is SATISFIABLE (true in some models).")
    else:
        print("\n□ Result: The formula is UNSATISFIABLE (false in all models).")

# === Example usage ===
if __name__ == "__main__":
    # This formula is satisfiable but not valid
    formula = "A and not B"
    model_checking(formula, max_seconds=5)
