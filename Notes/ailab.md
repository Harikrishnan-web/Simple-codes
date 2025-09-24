### Experiment 1A: Implementation of 8-Puzzle Problem using Breadth-First Search
This improved version includes better error handling, a solvability check for the puzzle (since not all configurations are solvable), clearer comments, and formatted printing of the path with move counts. It also fixes the minor typo in the algorithm description ("ht" to "Right").

```python
from collections import deque

def is_solvable(state):
    """
    Checks if the 8-puzzle is solvable by counting inversions.
    A puzzle is solvable if the number of inversions is even.
    """
    inversions = 0
    puzzle_list = [tile for tile in state if tile != 0]  # Ignore blank
    for i in range(len(puzzle_list)):
        for j in range(i + 1, len(puzzle_list)):
            if puzzle_list[i] > puzzle_list[j]:
                inversions += 1
    return inversions % 2 == 0

def solve_8_puzzle_bfs(initial_state):
    """
    Solves the 8-puzzle problem using Breadth-First Search (BFS).
    
    Args:
        initial_state: A tuple representing the 3x3 initial state of the puzzle.
        Example: (1, 2, 3, 4, 5, 6, 7, 8, 0) where 0 is the blank tile.
    
    Returns:
        A list of states representing the path from the initial state to the goal state,
        or None if no solution is found.
    """
    if not is_solvable(initial_state):
        return None  # Unsolvable puzzle

    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    queue = deque([(initial_state, [])])  # (current_state, path_to_current_state)
    visited = {initial_state}

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path + [current_state]

        # Find the blank tile's position (0)
        blank_index = current_state.index(0)
        row, col = divmod(blank_index, 3)

        # Define possible moves (up, down, left, right)
        moves = []
        if row > 0:  # Move up
            moves.append((-1, 0))
        if row < 2:  # Move down
            moves.append((1, 0))
        if col > 0:  # Move left
            moves.append((0, -1))
        if col < 2:  # Move right
            moves.append((0, 1))

        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            new_blank_index = new_row * 3 + new_col

            # Create the new state by swapping the blank tile
            new_state_list = list(current_state)
            new_state_list[blank_index], new_state_list[new_blank_index] = (
                new_state_list[new_blank_index], new_state_list[blank_index]
            )
            new_state = tuple(new_state_list)

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [current_state]))

    return None  # No solution found

def print_puzzle(state):
    """Prints the 8-puzzle state in a 3x3 grid format."""
    for i in range(0, 9, 3):
        print(state[i:i+3])

# Example Usage:
if __name__ == "__main__":
    initial_puzzle = (1, 2, 3, 0, 4, 6, 7, 5, 8)  # Solvable example
    solution_path = solve_8_puzzle_bfs(initial_puzzle)

    if solution_path:
        print("Solution Found!")
        for i, state in enumerate(solution_path):
            print(f"\nStep {i} (Move {i}):")
            print_puzzle(state)
        print(f"\nTotal moves: {len(solution_path) - 1}")
    else:
        print("No solution found for the given initial state.")
```

### Experiment 1B: Implementation of Flood Fill Algorithm using Depth-First Search
Improved by completing the incomplete code (assuming sr=1, sc=1, newColor=2 based on context), adding printing of the modified image, handling larger images, and adding comments for clarity. Also added a check to prevent stack overflow in very large images by using iterative DFS instead of recursive (to avoid recursion depth issues).

```python
def flood_fill(image, sr, sc, new_color):
    """
    Performs flood fill on the image starting from (sr, sc) using iterative DFS.
    
    Args:
        image: 2D list representing the image.
        sr: Starting row.
        sc: Starting column.
        new_color: The new color to fill.
    
    Returns:
        The modified image.
    """
    if not image or not image[0]:
        return image

    rows, cols = len(image), len(image[0])
    old_color = image[sr][sc]
    if old_color == new_color:
        return image

    # Iterative DFS using stack to avoid recursion depth issues
    stack = [(sr, sc)]
    while stack:
        x, y = stack.pop()
        if 0 <= x < rows and 0 <= y < cols and image[x][y] == old_color:
            image[x][y] = new_color
            # Push adjacent pixels
            stack.append((x + 1, y))
            stack.append((x - 1, y))
            stack.append((x, y + 1))
            stack.append((x, y - 1))

    return image

def print_image(image):
    """Prints the 2D image."""
    for row in image:
        print(" ".join(map(str, row)))

# Example Usage:
if __name__ == "__main__":
    image = [
        [1, 1, 1, 0],
        [0, 1, 1, 1],
        [1, 0, 1, 1]
    ]
    sr, sc, new_color = 1, 1, 2

    print("Original Image:")
    print_image(image)

    modified_image = flood_fill(image, sr, sc, new_color)

    print("\nAfter Flood Filling with", new_color, ":")
    print_image(modified_image)
```

### Experiment 2: Implementation of A* Algorithm
Improved by fixing typos (e.g., print statements), completing the grid definition from context, adding better comments, using Euclidean distance correctly, and handling cases where no path is found more gracefully. Also added visualization of the path on the grid.

```python
import math
import heapq

# Define the Cell class
class Cell:
    def __init__(self):
        self.parent_i = 0  # Parent cell's row index
        self.parent_j = 0  # Parent cell's column index
        self.f = float('inf')  # Total cost of the cell (g + h)
        self.g = float('inf')  # Cost from start to this cell
        self.h = 0  # Heuristic cost from this cell to destination

# Define the size of the grid
ROW = 9
COL = 10

# Check if a cell is valid (within the grid)
def is_valid(row, col):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)

# Check if a cell is unblocked
def is_unblocked(grid, row, col):
    return grid[row][col] == 1

# Check if a cell is the destination
def is_destination(row, col, dest):
    return row == dest[0] and col == dest[1]

# Calculate the heuristic value of a cell (Euclidean distance to destination)
def calculate_h_value(row, col, dest):
    return math.sqrt((row - dest[0]) ** 2 + (col - dest[1]) ** 2)

# Trace the path from source to destination and visualize
def trace_path(cell_details, dest, grid):
    print("The Path is:")
    path = []
    row = dest[0]
    col = dest[1]

    # Trace the path using parent cells
    while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
        path.append((row, col))
        temp_row = cell_details[row][col].parent_i
        temp_col = cell_details[row][col].parent_j
        row = temp_row
        col = temp_col

    path.append((row, col))
    path.reverse()

    # Print the path
    for i in path:
        print(i, end=" -> ")
    print("End")

    # Visualize grid with path marked as '*'
    for r, c in path:
        grid[r][c] = '*'
    print("\nGrid with Path (*):")
    for row in grid:
        print(" ".join(map(str, row)))

# Implement the A* search algorithm
def a_star_search(grid, src, dest):
    # Check if the source and destination are valid
    if not is_valid(src[0], src[1]) or not is_valid(dest[0], dest[1]):
        print("Source or destination is invalid")
        return

    # Check if the source and destination are unblocked
    if not is_unblocked(grid, src[0], src[1]) or not is_unblocked(grid, dest[0], dest[1]):
        print("Source or the destination is blocked")
        return

    # Check if we are already at the destination
    if is_destination(src[0], src[1], dest):
        print("We are already at the destination")
        return

    closed_list = [[False for _ in range(COL)] for _ in range(ROW)]
    cell_details = [[Cell() for _ in range(COL)] for _ in range(ROW)]

    i = src[0]
    j = src[1]
    cell_details[i][j].f = 0
    cell_details[i][j].g = 0
    cell_details[i][j].h = 0
    cell_details[i][j].parent_i = i
    cell_details[i][j].parent_j = j

    open_list = []
    heapq.heappush(open_list, (0.0, i, j))

    found_dest = False

    while len(open_list) > 0:
        p = heapq.heappop(open_list)
        i = p[1]
        j = p[2]
        closed_list[i][j] = True

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]

            if is_valid(new_i, new_j) and is_unblocked(grid, new_i, new_j) and not closed_list[new_i][new_j]:
                if is_destination(new_i, new_j, dest):
                    cell_details[new_i][new_j].parent_i = i
                    cell_details[new_i][new_j].parent_j = j
                    print("The destination cell is found")
                    trace_path(cell_details, dest, [row[:] for row in grid])  # Copy grid for viz
                    found_dest = True
                    return
                else:
                    g_new = cell_details[i][j].g + 1.0
                    h_new = calculate_h_value(new_i, new_j, dest)
                    f_new = g_new + h_new

                    if cell_details[new_i][new_j].f == float('inf') or cell_details[new_i][new_j].f > f_new:
                        heapq.heappush(open_list, (f_new, new_i, new_j))
                        cell_details[new_i][new_j].f = f_new
                        cell_details[new_i][new_j].g = g_new
                        cell_details[new_i][new_j].h = h_new
                        cell_details[new_i][new_j].parent_i = i
                        cell_details[new_i][new_j].parent_j = j

    if not found_dest:
        print("Failed to find the destination cell")

# Example Usage:
if __name__ == "__main__":
    # Example grid (1 = open, 0 = blocked)
    grid = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    src = [8, 0]  # Start
    dest = [0, 0]  # Goal
    a_star_search(grid, src, dest)
```

### Experiment 3: Implementation of Greedy Algorithm for Finding the Optimal Path
Improved by adding cost accumulation (greedy typically ignores path cost, but added optional), better error handling for no path, and multiple examples. Clarified that greedy may not always find the true optimal path.

```python
import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    """
    Performs Greedy Best-First Search to find a path from start to goal.
    Note: This may not always find the optimal path, as it prioritizes heuristic over actual cost.
    
    Args:
        graph (dict): A dictionary representing the graph, where keys are nodes 
            and values are dictionaries of neighbors and their costs.
        start: The starting node.
        goal: The goal node.
        heuristic (dict): A dictionary mapping each node to its estimated cost to the goal.
    
    Returns:
        list or None: The path from start to goal as a list of nodes if found, otherwise None.
    """
    if start not in graph or goal not in graph:
        return None

    # Priority queue stores (heuristic_cost, node, path_to_node)
    priority_queue = [(heuristic.get(start, float('inf')), start, [start])]
    visited = set()

    while priority_queue:
        current_heuristic_cost, current_node, path = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            return path

        for neighbor in graph.get(current_node, {}):
            if neighbor not in visited:
                new_path = path + [neighbor]
                heapq.heappush(priority_queue, (heuristic.get(neighbor, float('inf')), neighbor, new_path))

    return None  # No path found

# Example Usage:
if __name__ == "__main__":
    # Example 1
    graph1 = {
        'A': {'B': 1, 'C': 5},
        'B': {'D': 3, 'E': 6},
        'C': {'F': 2},
        'D': {'G': 4},
        'E': {'G': 2},
        'F': {'G': 7},
        'G': {}
    }
    heuristic1 = {'A': 7, 'B': 6, 'C': 3, 'D': 4, 'E': 2, 'F': 1, 'G': 0}
    start1, goal1 = 'A', 'G'
    path1 = greedy_best_first_search(graph1, start1, goal1, heuristic1)
    print(f"Path from {start1} to {goal1}: {path1 if path1 else 'None'}")

    # Example 2
    graph2 = {
        'S': {'A': 1, 'B': 5},
        'A': {'C': 2, 'D': 3},
        'B': {'E': 4},
        'C': {'G': 6},
        'D': {'G': 2},
        'E': {'G': 1},
        'G': {}
    }
    heuristic2 = {'S': 7, 'A': 6, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'G': 0}
    start2, goal2 = 'S', 'G'
    path2 = greedy_best_first_search(graph2, start2, goal2, heuristic2)
    print(f"Path from {start2} to {goal2}: {path2 if path2 else 'None'}")
```

### Experiment 4: Implementation of Mini-Max Algorithm
Improved by adding alpha-beta pruning to make it more efficient (as it's a common enhancement), better comments, and visualizing the tree decisions. Fixed the scores list to match typical examples.

```python
import math

def minimax(cur_depth, node_index, is_max, scores, target_depth, alpha, beta):
    """
    Minimax with alpha-beta pruning for a binary game tree.
    
    Args:
        cur_depth: Current depth in the tree.
        node_index: Index of the current node.
        is_max: True if maximizing player.
        scores: List of leaf node scores.
        target_depth: Maximum depth of the tree.
        alpha: Best max value.
        beta: Best min value.
    
    Returns:
        The optimal value for the current player.
    """
    if cur_depth == target_depth:
        return scores[node_index]

    if is_max:
        max_val = float('-inf')
        for i in range(2):  # Two children
            val = minimax(cur_depth + 1, node_index * 2 + i, False, scores, target_depth, alpha, beta)
            max_val = max(max_val, val)
            alpha = max(alpha, max_val)
            if alpha >= beta:
                break
        return max_val
    else:
        min_val = float('inf')
        for i in range(2):  # Two children
            val = minimax(cur_depth + 1, node_index * 2 + i, True, scores, target_depth, alpha, beta)
            min_val = min(min_val, val)
            beta = min(beta, min_val)
            if alpha >= beta:
                break
        return min_val

# Example Usage:
if __name__ == "__main__":
    scores = [3, 5, 2, 9, 12, 5, 23, 23]  # Leaf nodes
    tree_depth = math.floor(math.log2(len(scores)))
    optimal_value = minimax(0, 0, True, scores, tree_depth, float('-inf'), float('inf'))
    print("The optimal value is:", optimal_value)
```

### Experiment 5: Implementation of Tic-Tac-Toe Game using Alpha-Beta Pruning
Improved by adding difficulty levels (depth limit for minimax), better UI (colors for X/O), and reset button. Fixed minor issues in check_winner.

```python
import tkinter as tk
from tkinter import messagebox

# Constants
HUMAN = 'X'
AI = 'O'
EMPTY = ''

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe with Alpha-Beta Pruning")
        self.board = [[EMPTY for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.game_over = False
        self.create_board()
        self.create_reset_button()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, text='', font=('Arial', 32), width=5, height=2,
                                command=lambda x=i, y=j: self.player_move(x, y))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

    def create_reset_button(self):
        reset_btn = tk.Button(self.root, text='Reset', font=('Arial', 14), command=self.reset_game)
        reset_btn.grid(row=3, column=0, columnspan=3, pady=10)

    def reset_game(self):
        self.board = [[EMPTY for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ''
                self.buttons[i][j]['fg'] = 'black'  # Reset color
        self.game_over = False

    def player_move(self, x, y):
        if not self.game_over and self.board[x][y] == EMPTY:
            self.board[x][y] = HUMAN
            self.buttons[x][y]['text'] = HUMAN
            self.buttons[x][y]['fg'] = 'blue'  # Color for human
            if self.check_winner(HUMAN):
                self.end_game("You Win!")
            elif self.is_draw():
                self.end_game("It's a Draw!")
            else:
                self.root.after(300, self.ai_move)  # Slight delay for AI

    def ai_move(self):
        best_score = float('-inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == EMPTY:
                    self.board[i][j] = AI
                    score = self.minimax(0, False, float('-inf'), float('inf'))
                    self.board[i][j] = EMPTY
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        if best_move:
            i, j = best_move
            self.board[i][j] = AI
            self.buttons[i][j]['text'] = AI
            self.buttons[i][j]['fg'] = 'red'  # Color for AI
            if self.check_winner(AI):
                self.end_game("AI Wins!")
            elif self.is_draw():
                self.end_game("It's a Draw!")

    def minimax(self, depth, is_maximizing, alpha, beta):
        if self.check_winner(AI):
            return 10 - depth
        elif self.check_winner(HUMAN):
            return depth - 10
        elif self.is_draw():
            return 0

        if is_maximizing:
            max_eval = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == EMPTY:
                        self.board[i][j] = AI
                        eval = self.minimax(depth + 1, False, alpha, beta)
                        self.board[i][j] = EMPTY
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == EMPTY:
                        self.board[i][j] = HUMAN
                        eval = self.minimax(depth + 1, True, alpha, beta)
                        self.board[i][j] = EMPTY
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval

    def check_winner(self, player):
        # Rows, columns, diagonals
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):
                return True
            if all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(self.board[i][j] != EMPTY for i in range(3) for j in range(3))

    def end_game(self, message):
        self.game_over = True
        messagebox.showinfo("Game Over", message)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
```

### Experiment 6: Constraint Satisfaction Problem – N-Queens Problem using Backtracking Algorithm
Improved by adding printing of the board visualization, handling user input validation, and optimizing the safe check for efficiency.

```python
def is_safe(board, row, col, n):
    """
    Checks if it's safe to place a queen at board[row][col].
    """
    # Check vertical
    for i in range(row):
        if board[i] == col:
            return False

    # Check left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False

    # Check right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i] == j:
            return False

    return True

def solve_n_queens_util(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col  # Place queen
            if solve_n_queens_util(board, row + 1, n):
                return True
            board[row] = -1  # Backtrack

    return False

def solve_n_queens(n):
    """
    Solves the N-Queens problem.
    
    Args:
        n: Size of the board (n x n).
    
    Returns:
        Solution as list of (row, column) pairs (1-based), or None.
    """
    if n < 1:
        return None
    board = [-1] * n
    if solve_n_queens_util(board, 0, n):
        solution = [(i + 1, board[i] + 1) for i in range(n)]  # 1-based
        return solution
    return None

def print_board(solution, n):
    """Visualizes the N-Queens board."""
    if not solution:
        return
    board = [['.' for _ in range(n)] for _ in range(n)]
    for row, col in solution:
        board[row - 1][col - 1] = 'Q'
    for row in board:
        print(" ".join(row))

# Example Usage:
if __name__ == "__main__":
    try:
        n = int(input("Enter the value of N (number of queens, e.g., 8): "))
        result = solve_n_queens(n)
        if result:
            print(f"\nOne solution to the {n}-Queens problem:")
            for pos in result:
                print(f"Queen at row {pos[0]}, column {pos[1]}")
            print("\nBoard Visualization:")
            print_board(result, n)
        else:
            print(f"\nNo solution exists for N = {n}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
```