# Artificial Intelligence - Unit III Notes
## Game Playing and Constraint Satisfaction Problems (CSP)

---

## 1. Adversarial Search and Games

Adversarial search problems occur in **multi-agent environments** where agents have conflicting goals (e.g., Chess, Go, Poker).  
We analyze these using **Game Theory**.

### 1.1 Game Theory
- Models interactions between **rational agents** (players).
- **Types of games studied in AI**: deterministic, two-player, turn-taking, perfect information, zero-sum games.
  - *Deterministic*: No randomness in state transitions.
  - *Two-player*: MAX vs MIN.
  - *Perfect information*: Both players know the state of the game.
  - *Zero-sum*: One player's gain is another's loss.

**Game components:**
- `S0`: Initial state  
- `PLAYER(s)`: Whose turn it is  
- `ACTIONS(s)`: Legal moves  
- `RESULT(s, a)`: Next state  
- `TERMINAL-TEST(s)`: Is the game over?  
- `UTILITY(s, p)`: Payoff for player p

**Example**: Tic-Tac-Toe game tree.

```
 Initial State
   |
   +-- X at (1,1)
   |
   +-- X at (1,2)
   |
   ...
```

Utility values: +1 (MAX wins), -1 (MIN wins), 0 (draw).

---

### 1.2 Optimal Decisions in Games
- **Minimax Algorithm**: chooses moves to maximize player’s minimum guaranteed utility.  
- **Conditional plans**: Strategy must handle all opponent responses.

**Two-ply game tree example:**

```
        MAX
      /  |  \
     a1  a2  a3
    /|   b1 b2 b3
```

- MIN chooses minimum values; MAX chooses maximum among them.

**Time complexity**: O(b^m)  
**Space complexity**: O(m)

---

### 1.3 Alpha–Beta Pruning
- Improves minimax by pruning branches that don’t affect the decision.
- Maintains two parameters:  
  - α (alpha): best option for MAX so far ("at least")  
  - β (beta): best option for MIN so far ("at most")

**Key Idea:**  
If a node is worse than a previously explored option, stop exploring that branch.

```
        MAX
       /      α=3       β=2   → prune branch
```

- Best case (perfect move ordering): O(b^(m/2)) nodes explored.  
- Practical for Chess with move ordering + transposition tables.

---

### 1.4 Heuristic Alpha–Beta Tree Search
- **Cutoff test**: stop search at certain depth.  
- **Evaluation function**: estimates utility based on features (e.g., in chess: material value, mobility, king safety).  
- Avoids **horizon effect** with *quiescence search*.  
- Uses **iterative deepening** for time control.

---

### 1.5 Monte Carlo Tree Search (MCTS)
- Useful in games like **Go** (large branching factor).  
- Replaces evaluation function with **random playouts** (simulations).  
- Four steps: **Selection → Expansion → Simulation → Backpropagation**.  
- Uses **UCT (Upper Confidence Bounds for Trees)** for balancing exploration vs exploitation.

---

### 1.6 Stochastic Games
- Games with randomness (dice, shuffling cards).  
- Example: **Backgammon**.  
- Use **Expectiminimax**: extends minimax with chance nodes.  
- Computes **expected utility** of moves.

---

### 1.7 Partially Observable Games
- Players do not see the full state (hidden info).  
- Example: **Poker, Kriegspiel (invisible chess)**.  
- Use **belief states**: probability distribution over possible states.  
- Strategies often involve **randomization** to avoid predictability.

---

## 2. Constraint Satisfaction Problems (CSP)

A **CSP** is defined by:  
- **Variables**: X1, X2, …, Xn  
- **Domains**: D1, D2, …, Dn (possible values)  
- **Constraints**: specify allowable combinations

**Example: Map Coloring**  
- Variables = regions  
- Domain = {Red, Green, Blue}  
- Constraints = adjacent regions ≠ same color

---

### 2.1 Constraint Propagation
- Uses inference to reduce domains.  
- **Arc consistency (AC-3 algorithm)**: ensures every value of Xi has a consistent value in Xj.  
- Detects early failure.

---

### 2.2 Backtracking Search
- Standard search for CSPs.  
- Improves with heuristics:  
  - **MRV (Minimum Remaining Values)** – choose variable with fewest legal values.  
  - **Degree heuristic** – choose variable involved in most constraints.  
  - **LCV (Least Constraining Value)** – pick value that rules out fewest choices.

---

### 2.3 Local Search for CSP
- Example: **Min-Conflicts heuristic** (effective for n-Queens).  
- Start with complete assignment, repair conflicts until solved.

---

### 2.4 Structure of CSP
- Some CSPs can be solved efficiently by exploiting structure.  
- **Tree-structured CSPs**: solvable in linear time.  
- **Cutset conditioning**: choose variables to break cycles.  
- **Symmetry detection**: reduces redundant search.

---

## Quick Revision Summary
- **Minimax** → optimal decision rule.  
- **Alpha–Beta** → efficient minimax.  
- **Heuristic Search** → evaluation + cutoff.  
- **MCTS** → simulations instead of heuristics.  
- **Expectiminimax** → stochastic games.  
- **Belief states** → partially observable games.  
- **CSP methods** → propagation, backtracking + heuristics, local search, exploiting structure.

