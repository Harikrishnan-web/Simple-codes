import random

# Graph: South Indian states and their neighbors
neighbors = {
    'TN': ['KL', 'KA', 'AP'],
    'KL': ['TN', 'KA'],
    'KA': ['KL', 'TN', 'AP', 'TG'],
    'AP': ['TN', 'KA', 'TG'],
    'TG': ['KA', 'AP']
}

colors = ['Red', 'Green', 'Blue']  # Try with 3 colors

def count_conflicts(assignment, neighbors):
    """Count the total number of conflicts in the current assignment."""
    conflicts = 0
    for region in neighbors:
        for neighbor in neighbors[region]:
            if assignment[region] == assignment.get(neighbor):
                conflicts += 1
    return conflicts // 2  # Each conflict counted twice

def hill_climbing(neighbors, colors, max_steps=1000):
    # Step 1: Random initial assignment
    assignment = {region: random.choice(colors) for region in neighbors}

    for step in range(max_steps):
        current_conflicts = count_conflicts(assignment, neighbors)
        if current_conflicts == 0:
            return assignment

        improved = False
        for region in neighbors:
            min_conflict = current_conflicts
            best_color = assignment[region]  # Default to current color

            for color in colors:
                if color == assignment[region]:
                    continue
                # Try changing the color
                original = assignment[region]
                assignment[region] = color
                temp_conflict = count_conflicts(assignment, neighbors)
                assignment[region] = original  # revert change

                if temp_conflict < min_conflict:
                    best_color = color
                    min_conflict = temp_conflict
                    improved = True

            assignment[region] = best_color

        if not improved:
            break  # Local maximum reached

    # Final check
    if count_conflicts(assignment, neighbors) == 0:
        return assignment
    return None

# Run the algorithm
solution = hill_climbing(neighbors, colors)

# Output
if solution:
    print("Hill-Climbing Map Coloring Solution:")
    for state in sorted(solution):
        print(f"{state}: {solution[state]}")
else:
    print("No solution found (local maximum reached).")
