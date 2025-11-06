# UNIT IV - LOGICAL REASONING: Quick Exam Revision Guide

## 1. KNOWLEDGE-BASED AGENTS

**Key Concept**: Agents that use internal knowledge representation and reasoning to decide actions.

**Components**:
- **Knowledge Base (KB)**: Set of sentences in a knowledge representation language
- **TELL**: Add new sentences to KB
- **ASK**: Query what is known
- **Operations involve inference**: Deriving new sentences from existing ones

**Agent Cycle**:
1. TELL KB what it perceives
2. ASK KB what action to perform
3. TELL KB which action was executed

## 2. PROPOSITIONAL LOGIC

### Syntax
**Atomic Sentences**: Single proposition symbols (P, Q, R, W₁,₃)
- **True**: Always true
- **False**: Always false

**Logical Connectives**:
1. **¬** (NOT/Negation)
2. **∧** (AND/Conjunction)
3. **∨** (OR/Disjunction)
4. **→** (Implication)
5. **⇔** (Biconditional)

### Key Concepts
- **Model**: Mathematical abstraction with fixed truth values
- **Entailment (α ⊨ β)**: α entails β if β is true in all models where α is true
- **Logical Equivalence (α ≡ β)**: True in same set of models

### Inference Rules
1. **Modus Ponens**: From α → β and α, infer β
2. **And-Elimination**: From (α ∧ β), infer α or β
3. **Resolution**: Most powerful rule for complete inference

### Limitations
- Cannot represent "all", "some", "none"
- Limited expressive power
- Cannot describe relationships between objects

## 3. FIRST-ORDER LOGIC (FOL)

### Elements
- **Constants**: A, B, John, 1, 2...
- **Variables**: x, y, z...
- **Predicates**: Brother(x,y), Father(x)...
- **Functions**: FatherOf(x)...
- **Quantifiers**:
  - **Universal (∀)**: "for all" - use with → (implication)
  - **Existential (∃)**: "there exists" - use with ∧ (and)

### Examples
- "All birds fly": ∀x bird(x) → fly(x)
- "Some boys play cricket": ∃x boys(x) ∧ play(x, cricket)

### FOL Inference Rules
1. **Universal Generalization**: P(c) ⟹ ∀x P(x)
2. **Universal Instantiation**: ∀x P(x) ⟹ P(c)
3. **Existential Instantiation**: ∃x P(x) ⟹ P(c) (new constant c)
4. **Existential Introduction**: P(c) ⟹ ∃x P(x)
5. **Generalized Modus Ponens**: Lifted version for FOL

## 4. RESOLUTION

### CNF Conversion Steps
1. Eliminate implications (→): Replace α → β with ¬α ∨ β
2. Move negation inwards (De Morgan's laws)
3. Standardize variables (rename to avoid conflicts)
4. Eliminate existential quantifiers (Skolemization)
5. Drop universal quantifiers
6. Distribute ∨ over ∧

### Resolution Algorithm
1. Convert KB and ¬goal to CNF
2. Apply resolution rule to complementary literals
3. Continue until:
   - **Empty clause found** → KB entails goal (PROVED)
   - **No new clauses** → KB doesn't entail goal

**Resolution Rule**: [l₁ ∨ ... ∨ lₙ] and [¬l₁ ∨ m₁ ∨ ... ∨ mₖ] → [l₂ ∨ ... ∨ lₙ ∨ m₁ ∨ ... ∨ mₖ]

## 5. FORWARD & BACKWARD CHAINING

### Forward Chaining (Data-Driven)
- **Start**: Known facts
- **Process**: Apply rules whose premises are satisfied
- **Direction**: Bottom-up (facts → goal)
- **Use**: Expert systems, continuous reasoning
- **Complexity**: Linear time

### Backward Chaining (Goal-Driven)
- **Start**: Goal/query
- **Process**: Find rules that conclude the goal, prove their premises
- **Direction**: Top-down (goal → facts)
- **Use**: Question answering, specific queries
- **Complexity**: Often less than linear (only touches relevant facts)

## 6. KNOWLEDGE REPRESENTATION

### Types of Knowledge
1. **Declarative**: Facts, concepts (what)
2. **Procedural**: How to do things (rules, strategies)
3. **Meta-knowledge**: Knowledge about knowledge
4. **Heuristic**: Expert rules of thumb
5. **Structural**: Relationships between concepts

### Approaches
1. **Simple Relational**: Tables/databases
2. **Inheritable**: Class hierarchies with inheritance
3. **Inferential**: Formal logic
4. **Procedural**: If-Then rules, code

## QUICK EXAM TIPS

### For Part A (Short Answers)
- **Knowledge Base**: Set of sentences representing world knowledge
- **Modus Ponens**: α → β, α ⟹ β
- **Atomic Sentence**: Single proposition symbol or predicate with terms
- **And-Elimination**: α ∧ β ⟹ α (or β)

### For Part B (Long Answers)
**Propositional Logic**: Explain syntax, semantics, truth tables, limitations

**Forward Chaining**: Algorithm + example with rule firing sequence

**Backward Chaining**: Algorithm + example working backwards from goal

**FOL vs Propositional**: FOL has objects, relations, functions, quantifiers; more expressive

**Resolution**: CNF conversion steps + resolution graph example

**Horn Clauses**: Form (P₁ ∧ P₂ ∧ ... ∧ Pₙ) → Q; enables efficient inference

### Common Question Patterns
1. Convert English to FOL
2. Prove using resolution (negate goal, show contradiction)
3. Draw forward/backward chaining trace
4. CNF conversion
5. Knowledge representation approaches

**Remember**: Resolution is **complete** for FOL. Forward chaining is **data-driven**. Backward chaining is **goal-driven**. Always check quantifier usage: ∀ with →, ∃ with ∧!