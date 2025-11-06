# UNIT V - PROBABILISTIC REASONING: Comprehensive Exam Revision Guide

## 1. ACTING UNDER UNCERTAINTY

### Why Uncertainty Arises
**Three Main Reasons (LAZINESS, THEORETICAL IGNORANCE, PRACTICAL IGNORANCE)**:

1. **Laziness**: Too much work to list complete antecedents/consequents for exception-less rules
2. **Theoretical Ignorance**: No complete theory exists for the domain (e.g., medical science)
3. **Practical Ignorance**: Cannot run all necessary tests; incomplete information about specific cases

**Example - Dental Diagnosis**:
- Simple rule: `Toothache ⇒ Cavity` is WRONG
- Reality: `Toothache ⇒ Cavity ∨ GumProblem ∨ Abscess...` (endless list)
- Causal rule: `Cavity ⇒ Toothache` is also WRONG (not all cavities cause pain)

### Logical Qualification Problem
- Logical agents need absolute certainty
- Example: Taxi to airport - "Plan A₉₀ works IF car doesn't break, no accident, road not closed, no meteorite..."
- Cannot deduce success with certainty → need probabilistic reasoning

### Ontological vs Epistemological Commitments
- **Logic**: Each sentence is true, false, or unknown
- **Probability**: Numerical degree of belief between 0 (certainly false) and 1 (certainly true)

### Decision Theory
**Formula**: `Decision Theory = Probability Theory + Utility Theory`

**Key Concepts**:
- **Utility**: Degree of usefulness of a state to an agent (relative to agent)
- **Maximum Expected Utility (MEU)**: Choose action with highest expected utility
- **Expected Utility** = Average of outcome utilities, weighted by probability

**Example**: Plans A₉₀ (97% success), A₁₈₀ (higher probability), A₁₄₄₀ (almost certain but intolerable wait)

---

## 2. BASIC PROBABILITY NOTATION

### Fundamental Concepts

**Sample Space (Ω)**: Set of all possible worlds
- Mutually exclusive and exhaustive
- Example: Rolling two dice → 36 possible worlds: (1,1), (1,2), ..., (6,6)

**Probability Model**: P(ω) for each possible world
**Axioms**:
1. 0 ≤ P(ω) ≤ 1 for all ω
2. Σ P(ω) = 1 (sum over all possible worlds)

### Types of Probability

**1. Unconditional/Prior Probability P(a)**:
- Degree of belief WITHOUT other information
- Example: P(Total = 11) = P((5,6)) + P((6,5)) = 1/36 + 1/36 = 1/18

**2. Conditional/Posterior Probability P(a|b)**:
- Probability of 'a' GIVEN evidence 'b'
- **Definition**: `P(a|b) = P(a ∧ b) / P(b)` where P(b) > 0

**Product Rule**: `P(a ∧ b) = P(a|b) × P(b) = P(b|a) × P(a)`

### Random Variables
- Names start with UPPERCASE (Total, Die1, Weather)
- Values are lowercase
- **Domain**: Set of possible values
- **Discrete**: Finite or countable (dice rolls)
- **Continuous**: Real numbers (temperature)

### Probability Distribution P(X)
- Vector of probabilities for all values of X
- Bold **P** indicates distribution
- Example: **P**(Weather) = ⟨0.6, 0.1, 0.29, 0.01⟩ for ⟨sun, rain, cloud, snow⟩

### Important Rules

**Negation**: `P(¬a) = 1 - P(a)`

**Inclusion-Exclusion**: `P(a ∨ b) = P(a) + P(b) - P(a ∧ b)`

**Marginalization (Summing Out)**:
```
P(Y) = Σz P(Y, z)
```
Sum over all possible values of Z to eliminate it

**Conditioning**:
```
P(Y) = Σz P(Y|z) × P(z)
```

**Normalization**:
```
P(Cavity|toothache) = α⟨P(cavity, toothache), P(¬cavity, toothache)⟩
```
Where α makes probabilities sum to 1

---

## 3. INFERENCE USING FULL JOINT DISTRIBUTIONS

### Full Joint Distribution
- Specifies P(X₁, X₂, ..., Xₙ) for ALL variable combinations
- For n Boolean variables: 2ⁿ entries
- **Probabilities must sum to 1**

**Example - Toothache, Cavity, Catch World**:
- 2 × 2 × 2 = 8 entries
- Can answer ANY query by summing relevant entries

### Computing Probabilities

**Marginal Probability**:
```
P(cavity) = Σ entries where cavity is true
         = 0.108 + 0.012 + 0.072 + 0.008 = 0.2
```

**Conditional Probability**:
```
P(cavity|toothache) = P(cavity ∧ toothache) / P(toothache)
                    = 0.12 / (0.12 + 0.08) = 0.6
```

**Using Normalization**:
```
P(Cavity|toothache) = α⟨0.12, 0.08⟩ = ⟨0.6, 0.4⟩
```

### Problems with Full Joint Distribution
- **Exponential size**: 2ⁿ entries for n Boolean variables
- **Intractable** for large domains
- **Solution**: Use independence and conditional independence

---

## 4. INDEPENDENCE

### Absolute Independence
**Definition**: `P(a|b) = P(a)` OR `P(a ∧ b) = P(a) × P(b)`

**Example**: Weather is independent of dental problems
```
P(Toothache, Catch, Cavity, Weather) 
  = P(Toothache, Catch, Cavity) × P(Weather)
```

**Reduces**: 32-element table → 8-element + 4-element tables

### Conditional Independence
**Most Important Concept for Bayesian Networks**

**Definition**: X is conditionally independent of Y given Z
```
P(X|Y, Z) = P(X|Z)
OR
P(X, Y|Z) = P(X|Z) × P(Y|Z)
```

**Notation**: X ⊥ Y | Z

**Example**: Toothache and Catch are independent given Cavity
```
P(toothache|catch, cavity) = P(toothache|cavity)
```

---

## 5. BAYES' RULE AND ITS USE

### Bayes' Rule (MOST IMPORTANT FORMULA)

**Basic Form**:
```
P(b|a) = P(a|b) × P(b) / P(a)
```

**With Normalization**:
```
P(Y|X) = α × P(X|Y) × P(Y)
```

**General Form (multivalued variables)**:
```
P(Y|X) = P(X|Y) × P(Y) / P(X)
```

**Conditionalized on Evidence**:
```
P(Y|X, e) = α × P(X|Y, e) × P(Y|e)
```

### Why Bayes' Rule is Useful

**Causal vs Diagnostic Direction**:
- **Causal**: P(effect|cause) - usually known
- **Diagnostic**: P(cause|effect) - what we want to compute

**Example - Medical Diagnosis**:
```
Given:
- P(stiffneck|meningitis) = 0.7 (causal - doctor knows this)
- P(meningitis) = 1/50,000 (prior)
- P(stiffneck) = 0.01 (prior)

Want: P(meningitis|stiffneck) (diagnostic)

Solution:
P(meningitis|stiffneck) = 0.7 × (1/50000) / 0.01
                        = 0.0014 or 0.14%
```

**Key Insight**: Even though stiffneck strongly indicates meningitis (70%), actual probability is small (0.14%) because base rate of meningitis is very low!

### Applications
1. Robot next-step calculation
2. Weather forecasting
3. Monty Hall problem
4. Medical diagnosis
5. Spam filtering

---

## 6. NAIVE BAYES MODELS

### Structure
**Single cause influences multiple conditionally independent effects**

**Formula**:
```
P(Cause, Effect₁, ..., Effectₙ) 
  = P(Cause) × Π P(Effectᵢ|Cause)
```

### Inference with Naive Bayes
```
P(Cause|e₁, ..., eₙ) = α × P(Cause) × Π P(eᵢ|Cause)
```

**Steps**:
1. For each possible cause value
2. Multiply prior P(Cause) by product of P(observed effects|Cause)
3. Normalize result

**Complexity**: Linear in number of observed effects (very efficient!)

### Text Classification Example

**Task**: Classify document into categories (news, sports, business, weather, entertainment)

**Variables**:
- Category (cause)
- HasWordᵢ (effects) - presence/absence of keywords

**Training**:
- P(Category = c) = fraction of documents in category c
- P(HasWordᵢ|Category = c) = fraction of category c documents containing word i

**Classification**:
1. Check which keywords appear in new document
2. Compute P(Category|observed words) using naive Bayes formula
3. Choose category with highest posterior probability

**Independence Assumption**: Words occur independently given category
- **Violated in practice** (e.g., "first quarter" more likely together)
- **Still works well** - ranking of categories often accurate
- Model tends to be overconfident (probabilities too close to 0 or 1)

**Applications**: Spam filtering, language detection, document retrieval, sentiment analysis

---

## 7. BAYESIAN NETWORKS (BELIEF NETWORKS)

### Definition
**Directed Acyclic Graph (DAG)** representing conditional dependencies

### Components

**1. Structure (Topology)**:
- **Nodes**: Random variables (discrete or continuous)
- **Edges**: Directed arrows showing dependencies
- **Parent-Child**: Arrow from X to Y → X is parent of Y
- **No cycles**: Hence "acyclic"

**2. Parameters**:
- Each node Xᵢ has **Conditional Probability Table (CPT)**: θ(Xᵢ|Parents(Xᵢ))
- For Boolean variable with k Boolean parents: 2^k probabilities

### Semantics

**Joint Probability Decomposition**:
```
P(X₁, ..., Xₙ) = Π P(Xᵢ|Parents(Xᵢ))
```

**Two Interpretations**:
1. **As joint distribution representation** (helps construction)
2. **As conditional independence statements** (helps inference)

### Classic Example: Burglar Alarm Network

**Variables**:
- Burglary (B)
- Earthquake (E)
- Alarm (A)
- JohnCalls (J)
- MaryCalls (M)

**Structure**:
```
Burglary → Alarm ← Earthquake
           ↓    ↓
       JohnCalls MaryCalls
```

**Conditional Independencies**:
- B ⊥ E (burglary independent of earthquake)
- J ⊥ M | A (calls independent given alarm)
- J ⊥ {B,E} | A (John doesn't perceive B or E directly)

**CPT Examples**:
```
P(B) = 0.001
P(E) = 0.002
P(A|B,E): varies from 0.95 (B,¬E) to 0.001 (¬B,¬E)
P(J|A) = 0.90, P(J|¬A) = 0.05
```

**Query Example**: P(B|J=true, M=true)
```
= α × P(B) × Σₑ Σₐ P(E) × P(A|B,E) × P(J|A) × P(M|A)
```

### Constructing Bayesian Networks

**Process**:
1. Choose variables
2. Choose ordering (causes before effects works best)
3. Add nodes in order
4. For each node, add edges from existing nodes that directly influence it
5. Specify CPT for each node

**Advantages**:
- **Compact**: Exploits conditional independence
- **Modular**: Local probability specifications
- **Natural**: Represents causal structure
- **Efficient inference**: Exploits network structure

---

## 8. EXACT INFERENCE IN BAYESIAN NETWORKS

### Two Inference Tasks

**Task 1: Evaluate Joint Probability**
```
P(x₁, ..., xₙ) = Π P(xᵢ|parents(xᵢ))
```
- Use factorized form
- Marginalize unwanted variables
- Use log probabilities to avoid underflow

**Task 2: Conditional Probability Queries**
```
P(X|e) = P(X, e) / P(e) = α × P(X, e)
```

### Inference by Enumeration

**Formula**:
```
P(X|e) = α × Σᵧ P(X, e, Y)
```
Where Y are hidden (non-evidence, non-query) variables

**Steps**:
1. For each value of X
2. Sum over all combinations of Y
3. Evaluate using chain rule
4. Normalize

**Problem**: Exponential in number of hidden variables!

### Variable Elimination (More Efficient)

**Key Idea**: Rearrange summations to marginalize variables one at a time

**Process**:
1. Choose elimination ordering
2. For each variable to eliminate:
   - Collect all factors mentioning it
   - Multiply them together
   - Sum out the variable
   - Store resulting factor
3. Multiply remaining factors
4. Normalize

**Complexity**: Depends on elimination order and network structure

**Example**:
```
P(B|J,M) = α × Σₑ Σₐ P(B) × P(E) × P(A|B,E) × P(J|A) × P(M|A)

Can rearrange as:
= α × P(B) × Σₑ P(E) × Σₐ P(A|B,E) × P(J|A) × P(M|A)
```

### Complexity Issues
- Exact inference is **#P-hard** (harder than NP-complete)
- Exponential worst case for multiply-connected networks
- Need approximate methods for large networks

---

## 9. APPROXIMATE INFERENCE

### Why Approximate Inference?
- Exact inference intractable for large networks
- Variable elimination can have exponential complexity
- Trade accuracy for computational efficiency

### Direct Sampling Methods

**1. Prior Sampling (Basic Monte Carlo)**:
```
for i = 1 to N:
    for each variable Xᵢ in topological order:
        sample xᵢ from P(Xᵢ|parents(xᵢ))
```
- Frequency converges to true probability
- Unbiased but can be slow

**2. Rejection Sampling**:
```
P(X|e) ≈ count(X, e) / count(e)
```
**Process**:
1. Generate samples using prior sampling
2. **Reject** samples inconsistent with evidence e
3. Estimate P(X|e) from remaining samples

**Problem**: Many samples rejected when P(e) is small → inefficient

**3. Likelihood Weighting**:
**Key Idea**: Fix evidence variables, sample others, weight by likelihood

**Process**:
1. Set evidence variables to observed values
2. Sample non-evidence variables given parents
3. Weight sample by w = Π P(eᵢ|parents(eᵢ))
4. Estimate P(X|e) = Σ w × [X in sample] / Σ w

**Advantages**:
- No sample rejection
- More efficient than rejection sampling
- Weighted samples account for evidence

### Markov Chain Monte Carlo (MCMC)

**Markov Chain Sampling**:
- Generate samples by making random changes to previous sample
- Use **Markov Blanket** to decide changes

**Markov Blanket of X**:
- Parents of X
- Children of X
- Other parents of X's children

**Property**: X conditionally independent of all other variables given its Markov Blanket

**Algorithm**:
1. Start with random state
2. For each iteration:
   - Select variable X
   - Sample new value from P(X|MarkovBlanket(X))
3. Collect samples after burn-in period
4. Estimate probabilities from sample frequencies

**Advantages**:
- Converges to true posterior (eventually)
- No need to fix evidence variables
- Works well for large networks

---

## 10. CAUSAL NETWORKS

### Definition
**Bayesian network where edges represent causal relationships**

### Difference from Regular Bayesian Networks
- Regular BN: Edges represent conditional dependence (not necessarily causal)
- Causal Network: Edges MUST represent causation

**Example**: These are equivalent Bayesian networks but different causal networks:
```
A → B → C  vs  A ← B ← C
```

### Interventions (do-calculus)

**Key Concept**: **do(X=x)** means actively setting X to x (intervention)

**Effect of Intervention**:
1. Cut all edges FROM parents TO X
2. Set X = x
3. Recompute probabilities

**Notation**:
- P(Y|X=x): Observation (seeing X=x)
- P(Y|do(X=x)): Intervention (forcing X=x)

**Example - Burglar Alarm**:
- P(Earthquake|Alarm=true) ≠ 0.002 (alarm suggests earthquake)
- P(Earthquake|do(Alarm=true)) = 0.002 (forcing alarm doesn't cause earthquake)

### Applications
- Predicting effects of interventions from observational data
- Determining causality vs correlation
- Policy decisions (what happens if we do X?)
- Medical treatments (effect of treatment vs correlation)

---

## QUICK REFERENCE FOR EXAM

### Key Formulas

**Bayes' Rule**: `P(Y|X) = α × P(X|Y) × P(Y)`

**Joint Distribution**: `P(X₁,...,Xₙ) = Π P(Xᵢ|Parents(Xᵢ))`

**Naive Bayes**: `P(Cause|e₁,...,eₙ) = α × P(Cause) × Π P(eᵢ|Cause)`

**Marginalization**: `P(Y) = Σz P(Y,z)`

**Conditioning**: `P(Y) = Σz P(Y|z)×P(z)`

### Problem-Solving Strategies

**For Bayes' Rule Problems**:
1. Identify: cause, effect, evidence
2. List given: P(effect|cause), P(cause), P(effect)
3. Apply formula
4. Interpret result considering base rates

**For Bayesian Network Problems**:
1. Draw network structure
2. Identify conditional independencies
3. Write joint distribution factorization
4. Apply inference method (enumeration or variable elimination)

**For Text Classification**:
1. Identify category (cause) and features (effects)
2. Compute priors: P(Category)
3. Compute likelihoods: P(Feature|Category)
4. Apply naive Bayes formula
5. Choose highest posterior

### Common Exam Questions

1. **Why uncertainty?** → Laziness, Theoretical Ignorance, Practical Ignorance
2. **Bayes' Rule derivation** → From P(a|b) = P(a∧b)/P(b)
3. **Naive Bayes application** → Text classification step-by-step
4. **Bayesian Network construction** → Draw structure, write CPTs, compute query
5. **Exact vs Approximate inference** → When to use each, advantages/disadvantages
6. **Causal networks** → Difference from BN, interventions

**Remember**: Independence reduces exponential complexity to manageable size. This is the KEY insight for all probabilistic reasoning!