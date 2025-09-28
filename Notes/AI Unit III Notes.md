# AL3391 - Artificial Intelligence Unit III
## Game Playing and Constraint Satisfaction Problems

---

## 📖 Table of Contents

1. [Game Playing](#game-playing)
   - [Game Theory](#game-theory)
   - [Optimal Decisions in Games](#optimal-decisions)
   - [Minimax Algorithm](#minimax-algorithm)
   - [Alpha-Beta Pruning](#alpha-beta-pruning)
   - [Heuristic Alpha-Beta Search](#heuristic-search)
   - [Monte Carlo Tree Search](#monte-carlo)
   - [Stochastic Games](#stochastic-games)
   - [Partially Observable Games](#partially-observable)

2. [Constraint Satisfaction Problems](#constraint-satisfaction)
   - [Defining CSPs](#defining-csps)
   - [Constraint Propagation](#constraint-propagation)
   - [Backtracking Search](#backtracking-search)
   - [Local Search for CSPs](#local-search)
   - [Structure of CSPs](#structure-csps)

---

## 🎮 Game Playing {#game-playing}

### What is Adversarial Search?

Adversarial search explores competitive environments where two or more agents have conflicting goals. Unlike standard search problems, here we deal with an opponent who is actively trying to prevent us from reaching our goal.

**Key Characteristics:**
- Two or more agents with conflicting objectives
- Agents make alternating moves
- State of game is fully or partially observable
- Outcome affects all players (zero-sum or non-zero-sum)

---

### 🎯 Game Theory {#game-theory}

Game theory provides the mathematical framework for analyzing strategic interactions between rational decision-makers.

#### Three Approaches to Multi-Agent Environments:

1. **Economic Approach**: Treat agents in aggregate (market dynamics)
2. **Environmental Approach**: Consider adversaries as part of non-deterministic environment
3. **Adversarial Approach**: Explicitly model opponents using game-tree search

#### Two-Player Zero-Sum Games

**Definition**: Games where what's good for one player is equally bad for the other.

**Formal Definition Components:**
- **S₀**: Initial state (starting board position)
- **TO-MOVE(s)**: Player whose turn it is in state s
- **ACTIONS(s)**: Set of legal moves in state s
- **RESULT(s,a)**: Resulting state after action a in state s
- **IS-TERMINAL(s)**: True when game is over
- **UTILITY(s,p)**: Final numeric value for player p in terminal state s

---

### ⚖️ Optimal Decisions in Games {#optimal-decisions}

#### Minimax Algorithm {#minimax-algorithm}

The minimax algorithm finds the optimal move by assuming both players play perfectly.

**Core Concept:**
- MAX player tries to maximize utility
- MIN player tries to minimize utility (for MAX)

**Minimax Value Formula:**
```
MINIMAX(s) = {
  UTILITY(s)                           if IS-TERMINAL(s)
  max_{a∈ACTIONS(s)} MINIMAX(RESULT(s,a))  if TO-MOVE(s) = MAX
  min_{a∈ACTIONS(s)} MINIMAX(RESULT(s,a))  if TO-MOVE(s) = MIN
}
```

**Algorithm Properties:**
- **Time Complexity**: O(b^m) where b = branching factor, m = maximum depth
- **Space Complexity**: O(bm) for generating all actions, O(m) for one action at a time
- **Completeness**: Yes (finite tree)
- **Optimality**: Yes (against optimal opponent)

**Pseudocode:**
```python
function MINIMAX-SEARCH(game):
    player = TO-MOVE(game.INITIAL)
    value, move = MAX-VALUE(game.INITIAL, game)
    return move

function MAX-VALUE(state, game):
    if IS-TERMINAL(state):
        return UTILITY(state, MAX)
    v = -∞
    for each action in ACTIONS(state):
        v2, a2 = MIN-VALUE(RESULT(state, action), game)
        if v2 > v:
            v, move = v2, action
    return v, move

function MIN-VALUE(state, game):
    if IS-TERMINAL(state):
        return UTILITY(state, MAX)
    v = +∞
    for each action in ACTIONS(state):
        v2, a2 = MAX-VALUE(RESULT(state, action), game)
        if v2 < v:
            v, move = v2, action
    return v, move
```

---

### ✂️ Alpha-Beta Pruning {#alpha-beta-pruning}

Alpha-beta pruning eliminates branches that cannot influence the final decision.

**Key Parameters:**
- **α (alpha)**: Best value that MAX can guarantee so far
- **β (beta)**: Best value that MIN can guarantee so far

**Pruning Condition:**
- Prune when β ≤ α
- MIN node: if v ≤ α, prune remaining actions
- MAX node: if v ≥ β, prune remaining actions

**Algorithm:**
```python
function ALPHA-BETA-SEARCH(game):
    player = TO-MOVE(game.INITIAL)
    value, move = MAX-VALUE(game.INITIAL, game, -∞, +∞)
    return move

function MAX-VALUE(state, game, α, β):
    if IS-TERMINAL(state):
        return UTILITY(state, MAX)
    v = -∞
    for each action in ACTIONS(state):
        v2, a2 = MIN-VALUE(RESULT(state, action), game, α, β)
        if v2 > v:
            v, move = v2, action
        α = max(α, v)
        if v ≥ β:
            return v, move  # Prune
    return v, move

function MIN-VALUE(state, game, α, β):
    if IS-TERMINAL(state):
        return UTILITY(state, MAX)
    v = +∞
    for each action in ACTIONS(state):
        v2, a2 = MAX-VALUE(RESULT(state, action), game, α, β)
        if v2 < v:
            v, move = v2, action
        β = min(β, v)
        if v ≤ α:
            return v, move  # Prune
    return v, move
```

**Performance:**
- **Best Case**: O(b^(m/2)) - can search twice as deep
- **Random Ordering**: O(b^(3m/4))
- **Move Ordering**: Critical for performance

**Move Ordering Techniques:**
- Try captures first
- Try threats next
- Try forward moves before backward moves
- **Killer Move Heuristic**: Try moves that caused cutoffs before
- **Iterative Deepening**: Use previous search to order moves

---

### 🎯 Heuristic Alpha-Beta Search {#heuristic-search}

When we can't search to the end of the game, we use heuristic evaluation functions.

**Modified Minimax Formula:**
```
H-MINIMAX(s,d) = {
  UTILITY(s)                              if IS-TERMINAL(s)
  EVAL(s)                                 if IS-CUTOFF(s,d)
  max_{a} H-MINIMAX(RESULT(s,a), d+1)     if TO-MOVE(s) = MAX
  min_{a} H-MINIMAX(RESULT(s,a), d+1)     if TO-MOVE(s) = MIN
}
```

#### Evaluation Functions

**Requirements:**
1. Fast to compute
2. Strongly correlated with winning chances
3. UTILITY(loss) ≤ EVAL(s) ≤ UTILITY(win)

**Weighted Linear Function:**
```
EVAL(s) = w₁f₁(s) + w₂f₂(s) + ... + wₙfₙ(s)
```

**Chess Example:**
- Pawn = 1, Knight/Bishop = 3, Rook = 5, Queen = 9
- Additional features: pawn structure, king safety, piece mobility

#### Cutting Off Search

**Quiescence Search**: Only apply evaluation to "quiet" positions where no major changes are imminent (e.g., no captures pending).

**Horizon Effect**: When inevitable bad events are pushed beyond search depth.
- **Solution**: Singular extensions for clearly better moves

#### Forward Pruning

**Beam Search**: Consider only n best moves at each level.
**PROBCUT**: Probabilistically prune moves likely outside (α,β) window.
**Late Move Reduction**: Search later moves to reduced depth.

---

### 🎲 Monte Carlo Tree Search {#monte-carlo}

MCTS estimates state values through random simulations rather than heuristic evaluation.

**Four Phases (repeated):**

1. **SELECTION**: Choose path through tree using selection policy
2. **EXPANSION**: Add new child node to tree
3. **SIMULATION**: Play random game to completion (playout)
4. **BACK-PROPAGATION**: Update win statistics up to root

#### UCT (Upper Confidence Bounds for Trees)

**UCB1 Formula:**
```
UCB1(n) = (U(n)/N(n)) + C√(ln(N(PARENT(n)))/N(n))
```

Where:
- U(n) = total utility through node n
- N(n) = number of visits to node n
- C = exploration constant (√2 theoretically optimal)

**Algorithm:**
```python
function UCT-SEARCH(game):
    tree = {game.INITIAL}
    while time_remaining():
        leaf = SELECT(tree.root, game)
        child = EXPAND(leaf, game)
        result = SIMULATE(child, game)
        BACK-PROPAGATE(child, result)
    return best_child(tree.root)

function SELECT(node, game):
    while not IS-TERMINAL(node) and FULLY-EXPANDED(node):
        node = BEST-UCB1-CHILD(node)
    return node
```

**Advantages:**
- No need for domain knowledge
- Can handle high branching factors
- Anytime algorithm
- Less sensitive to evaluation errors

**Disadvantages:**
- May miss critical moves
- Slower for positions with obvious best moves

---

### 🎰 Stochastic Games {#stochastic-games}

Games with random elements (dice, card deals) require expectiminimax algorithm.

**Expectiminimax Formula:**
```
EXPECTIMINIMAX(n) = {
  UTILITY(n)                                    if IS-TERMINAL(n)
  max_{a} EXPECTIMINIMAX(RESULT(n,a))          if n is MAX node
  min_{a} EXPECTIMINIMAX(RESULT(n,a))          if n is MIN node
  Σ_r P(r) × EXPECTIMINIMAX(RESULT(n,r))      if n is chance node
}
```

**Key Points:**
- Chance nodes represent random events
- Probabilities must sum to 1
- Evaluation functions must return expected utilities
- Pruning is possible but more complex

**Time Complexity**: O(b^m × n^m) where n = number of possible random outcomes

---

### 👻 Partially Observable Games {#partially-observable}

Games where players don't have complete information about the game state.

#### Examples:
- **Kriegspiel**: Chess with invisible opponent pieces
- **Poker**: Hidden cards
- **Bridge**: Partially revealed hands

#### Key Concepts:

**Belief State**: Set of all possible actual game states consistent with observations.

**Strategy Types:**
- **Guaranteed checkmate**: Works regardless of actual hidden state
- **Probabilistic checkmate**: Works with probability 1 through randomization
- **Accidental checkmate**: Works only if hidden information is favorable

**Averaging Over Clairvoyance**: 
Assume perfect information and choose move that works best on average across all possible hidden states.

**Problems with Clairvoyance:**
- Ignores information gathering
- Doesn't consider opponent's uncertainty
- No bluffing in poker

---

## 🧩 Constraint Satisfaction Problems {#constraint-satisfaction}

CSPs represent problems where states are defined by variables with values, and solutions must satisfy constraints.

### 📝 Defining CSPs {#defining-csps}

**CSP Components:**
- **X**: Set of variables {X₁, X₂, ..., Xₙ}
- **D**: Set of domains {D₁, D₂, ..., Dₙ}
- **C**: Set of constraints specifying allowed value combinations

**Constraint Types:**
- **Unary**: Single variable (e.g., X ≠ green)
- **Binary**: Two variables (e.g., X ≠ Y)
- **Global**: Multiple variables (e.g., AllDiff(X₁,...,Xₙ))

#### Example: Map Coloring Australia

**Variables**: X = {WA, NT, Q, NSW, V, SA, T}
**Domains**: D = {red, green, blue} for all variables
**Constraints**: Adjacent regions must have different colors
- SA ≠ WA, SA ≠ NT, SA ≠ Q, SA ≠ NSW, SA ≠ V
- WA ≠ NT, NT ≠ Q, Q ≠ NSW, NSW ≠ V

#### Example: Cryptarithmetic (SEND + MORE = MONEY)

**Variables**: F, T, U, W, R, O, C₁, C₂, C₃
**Domains**: {0,1,2,...,9} for letters, {0,1} for carries
**Constraints**:
- AllDiff(F,T,U,W,R,O) - all letters different
- Column arithmetic constraints
- No leading zeros

---

### 🔄 Constraint Propagation {#constraint-propagation}

Use constraints to reduce domains before/during search.

#### Node Consistency
Variable is node-consistent if all domain values satisfy unary constraints.

#### Arc Consistency
Variable Xᵢ is arc-consistent with Xⱼ if for every value in Dᵢ there exists a value in Dⱼ that satisfies the constraint.

**AC-3 Algorithm:**
```python
function AC-3(csp):
    queue = all arcs in csp
    while queue not empty:
        (Xi, Xj) = queue.pop()
        if REVISE(csp, Xi, Xj):
            if size of Di = 0:
                return false
            for each Xk in NEIGHBORS[Xi] - {Xj}:
                queue.add((Xk, Xi))
    return true

function REVISE(csp, Xi, Xj):
    revised = false
    for each x in Di:
        if no value y in Dj satisfies constraint(Xi=x, Xj=y):
            delete x from Di
            revised = true
    return revised
```

#### Path Consistency
Set {Xi, Xj} is path-consistent with respect to Xₘ if for every consistent assignment to {Xi, Xj}, there exists a value for Xₘ satisfying constraints with both Xi and Xj.

#### K-Consistency
CSP is k-consistent if any consistent assignment to k-1 variables can be extended to any kth variable.
- 1-consistency = node consistency  
- 2-consistency = arc consistency
- 3-consistency = path consistency

#### Global Constraints

**AllDiff Consistency:**
If m variables have n total distinct values and m > n, constraint is violated.

**Resource Constraints (AtMost):**
AtMost(10, P₁, P₂, P₃, P₄) means P₁ + P₂ + P₃ + P₄ ≤ 10

---

### ⬅️ Backtracking Search {#backtracking-search}

**Basic Algorithm:**
```python
function BACKTRACKING-SEARCH(csp):
    return BACKTRACK({}, csp)

function BACKTRACK(assignment, csp):
    if assignment is complete:
        return assignment
    var = SELECT-UNASSIGNED-VARIABLE(csp)
    for each value in ORDER-DOMAIN-VALUES(var, assignment, csp):
        if value is consistent with assignment:
            add {var = value} to assignment
            inferences = INFERENCE(csp, var, value)
            if inferences ≠ failure:
                result = BACKTRACK(assignment, csp)
                if result ≠ failure:
                    return result
            remove {var = value} and inferences from assignment
    return failure
```

#### Heuristics

**Variable Ordering:**
1. **MRV (Minimum Remaining Values)**: Choose variable with fewest legal values
2. **Degree Heuristic**: Choose variable involved in most constraints (tie-breaker)

**Value Ordering:**
- **Least Constraining Value**: Choose value that rules out fewest options for neighboring variables

#### Inference During Search

**Forward Checking**: When variable X is assigned, establish arc consistency for all unassigned neighbors.

**MAC (Maintaining Arc Consistency)**: Run full AC-3 after each assignment.

#### Intelligent Backtracking

**Conflict-Directed Backjumping**: 
- Keep track of conflict set for each variable
- When domain becomes empty, backjump to most recent variable in conflict set
- More efficient than chronological backtracking

**Constraint Learning**:
- Record no-goods (combinations that lead to failure)
- Add constraints to prevent same failures later

---

### 🔄 Local Search for CSPs {#local-search}

Start with complete assignment and modify one variable at a time.

#### Min-Conflicts Algorithm
```python
function MIN-CONFLICTS(csp, max_steps):
    current = random complete assignment for csp
    for i = 1 to max_steps:
        if current is solution:
            return current
        var = randomly chosen conflicted variable
        value = value that minimizes conflicts with neighbors
        set var = value in current
    return failure
```

**Performance**: Very effective for many CSPs (e.g., n-queens solvable in ~50 steps even for n=1,000,000)

**Enhancements:**
- **Plateau Search**: Allow sideways moves
- **Tabu Search**: Maintain list of recently visited states
- **Simulated Annealing**: Accept bad moves with decreasing probability
- **Constraint Weighting**: Increase weights of frequently violated constraints

---

### 🌳 Structure of CSPs {#structure-csps}

#### Independent Subproblems
If constraint graph has disconnected components, solve each independently.
- Time: O(d^c × n/c) where c = size of largest component
- Much better than O(d^n) for full problem

#### Tree-Structured CSPs

**Properties:**
- Any two variables connected by exactly one path
- Can be solved in O(nd²) time

**Algorithm:**
1. Choose root and order variables (topological sort)
2. Make graph directional arc-consistent (bottom-up)
3. Assign values top-down (no backtracking needed)

#### Cutset Conditioning
1. Find cycle cutset S (removing S makes graph a tree)
2. Try all assignments to variables in S  
3. For each assignment, solve resulting tree-structured CSP
- Time: O(d^c × (n-c)d²) where c = |S|

#### Tree Decomposition
Transform constraint graph into tree where each node contains subset of variables.

**Requirements:**
1. Every variable appears in at least one tree node
2. If two variables are constrained, they appear together in some node  
3. If variable appears in two nodes, it appears in every node on path between them

**Tree Width**: Size of largest node minus 1
- Time: O(nd^(w+1)) where w = tree width

---

## 📚 Important Formulas Summary

### Game Playing
- **Minimax Time**: O(b^m)
- **Alpha-Beta Best Case**: O(b^(m/2))  
- **UCB1**: U(n)/N(n) + C√(ln(N(parent))/N(n))
- **Expectiminimax**: Σ P(r) × Value(r)

### CSP
- **Arc Consistency Time**: O(n²d³)
- **Tree CSP**: O(nd²) 
- **Cutset**: O(d^c × (n-c)d²)
- **Tree Decomposition**: O(nd^(w+1))

---

## 🎯 Exam Tips

### Likely Questions (13 marks):
1. Explain minimax and alpha-beta pruning with example
2. Describe Monte Carlo Tree Search algorithm
3. Solve cryptarithmetic problem (SEND+MORE=MONEY)
4. Explain constraint propagation techniques
5. Compare backtracking vs local search for CSPs

### Key Concepts to Remember:
- Alpha-beta pruning eliminates provably irrelevant branches
- MCTS uses simulations rather than evaluation functions
- Arc consistency can solve some CSPs without search
- Tree-structured CSPs are solvable in polynomial time
- Local search works well for CSPs with dense solution spaces

### Practice Problems:
- Work through minimax/alpha-beta on tic-tac-toe
- Apply AC-3 to simple CSPs
- Trace through backtracking with MRV heuristic
- Solve n-queens using min-conflicts