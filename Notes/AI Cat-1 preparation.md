

```markdown
# Artificial Intelligence - Unit 1: Intelligent Agents

---

## 1. Introduction to Artificial Intelligence (AI)

### What is AI?

Artificial Intelligence (AI) is a branch of computer science that aims to create intelligent machines capable of mimicking human-like behaviors such as thinking, learning, problem-solving, and decision-making.

- AI enables machines to operate with human intelligence.
- Machines can perform tasks like reasoning, learning, and understanding.

### Applications of AI

- Autonomous vehicles (e.g., self-driving cars)
- Virtual assistants (e.g., Siri, Google Assistant)
- Games (e.g., Chess, Go)
- Expert Systems (e.g., medical diagnosis tools)
- Robotics (e.g., manufacturing robots, humanoids)
- Personalized recommendations (e.g., Netflix, Amazon)

---

## 2. Why Study AI?

- Solve complex real-world problems efficiently (healthcare, traffic, marketing)
- Build machines that operate in risky environments (robots in hazardous zones)
- Enhance technological innovation and open new opportunities
- Develop virtual assistants and intelligent software systems

---

## 3. Goals of AI

- **Replicate human intelligence**: Machines that reason and think like humans
- **Solve knowledge-intensive tasks**: Domains requiring expert knowledge
- **Integrate perception and action**: Agent perceives environment and acts accordingly
- **Achieve complex human tasks**: Playing chess, driving, planning surgeries
- **Create learning systems**: Systems that learn and improve from experience

---

## 4. Components of AI

AI is interdisciplinary and involves:

- Mathematics (logic, probability)
- Computer Science (algorithms, programming)
- Psychology (human intelligence, cognition)
- Biology (neural networks)
- Sociology (social intelligence)
- Statistics (data analysis)
- Neuroscience (brain modeling)

---

## 5. Advantages and Disadvantages of AI

### Advantages

- High accuracy and low error rates
- Fast processing and decision-making
- Reliability and consistency
- Useful in risky or inaccessible environments
- Assisting humans through virtual assistants and automation

### Disadvantages

- High cost of systems and maintenance
- Limited creativity and inability to think "out of the box"
- Lack of emotions and empathy
- Increased dependency on machines
- Ethical and privacy concerns

---

## 6. History and Evolution of AI

- **Early Foundations (1940-1950s)**
  - Neural models (McCulloch-Pitts neuron, 1943)
  - Hebbian learning (1949)
  - Turing test proposed (1950)

- **Birth of AI (1956)**
  - Dartmouth conference coins "Artificial Intelligence"
  - First AI programs (Logic Theorist)

- **Golden Years (1960s-70s)**
  - Development of chatbots (ELIZA)
  - Robotics (WABOT-1)

- **AI Winters (1974-80, 1987-93)**
  - Funding reductions due to limited progress

- **Recent Progress (1990s-present)**
  - Successes: Deep Blue, Watson, AlphaGo
  - AI in everyday applications: virtual assistants, recommendation systems

---

## 7. Types of Artificial Intelligence

### Based on Capability

| Type        | Description                                                                 | Example                  |
|-------------|-----------------------------------------------------------------------------|--------------------------|
| **Weak AI** | AI systems designed for specific tasks without generalization                | Siri, Chess programs     |
| **General AI** | Hypothetical AI with human-like intelligence across multiple domains         | Still under research     |
| **Super AI** | Future AI surpassing human intelligence                                     | Theoretical concept      |

### Based on Functionality

| Type             | Description                                                         | Example                            |
|------------------|---------------------------------------------------------------------|----------------------------------|
| **Reactive**     | No memory of past, reacts only to current input                     | Deep Blue (Chess AI)              |
| **Limited Memory** | Uses limited historical data to improve decisions                  | Self-driving cars                 |
| **Theory of Mind** | Aimed at understanding emotions and beliefs (not yet developed)  | Research phase                   |
| **Self-aware**    | Possess human-like consciousness (theoretical/future AI)           | Hypothetical                     |

---

## 8. Intelligent Agents and Environments

### What is an Agent?

- An entity that perceives its environment through sensors and acts upon it using actuators.
- Examples:
  - Humans (sensors: eyes, ears; actuators: hands, legs)
  - Robots (cameras, motors)
  - Software agents (mouse inputs, keyboard; screen output)

### Agent Structure and Cycle

```
Perceive -> Reason -> Act -> Observe next percept
```

### Sensors and Actuators

- **Sensors**: Devices for perception (e.g., camera, microphone)
- **Actuators**: Components to perform actions (e.g., wheels, robotic arms)

---

## 9. Types of Agents

| Type                | Description                                                                                           |
|---------------------|----------------------------------------------------------------------------------------------------|
| **Simple Reflex Agent** | Acts only on current percepts; follows condition-action rules                                     |
| **Model-Based Agent**   | Maintains an internal state to handle partially observable environments                           |
| **Goal-Based Agent**    | Acts to achieve goals; anticipates future states and plans                                        |
| **Utility-Based Agent** | Chooses actions maximizing a utility function assessing desirability of states                    |
| **Learning Agent**      | Improves performance using learning from past experiences                                        |

---

## 10. Rationality in Agents

- **Rational agents** act to maximize the expected value of their performance measure.
- Rationality depends on:
  - Performance measure (criteria for success)
  - Prior knowledge about the environment
  - Available actions
  - Sequence of percepts to date

---

## 11. Types of Environments

| Feature          | Description                          | Example                        |
|------------------|------------------------------------|-------------------------------|
| **Observable**   | Fully or partially observable       | Fully: chess board; Partially: driving a car |
| **Deterministic**| Next state fully determined by current state and action | Chess is deterministic          |
| **Dynamic**      | Environment can change while agent deliberates | Driving car environment         |
| **Discrete**     | Finite number of percepts and actions | Chess moves                    |
| **Episodic**    | Each episode independent             | Multiple-choice questions       |
| **Single/Multi-Agent** | Environments with one or more agents | Chess (2 agents)               |

---

## 12. Agent Design: PEAS Model

- **P**: Performance measure (success criteria)
- **E**: Environment (where agent operates)
- **A**: Actuators (means of action)
- **S**: Sensors (means of perception)

### Example: Self-driving Car

| Element         | Example                                       |
|-----------------|-----------------------------------------------|
| Performance     | Safety, comfort, adherence to laws             |
| Environment    | Roads, traffic, pedestrians                     |
| Actuators      | Steering wheel, accelerator, brakes             |
| Sensors        | Cameras, lidar, GPS, speedometer                 |

---

## 13. Problem-Solving Agents and Search

### Problem Solving Overview

- A problem is defined by initial state, a set of actions, goal test, and path cost.
- Problem-solving agents use search strategies to find sequences of actions to reach goals.

### Search Algorithms

Two main types:

- **Uninformed (Blind) Search**: No extra info about states beyond problem definition
- **Informed (Heuristic) Search**: Uses heuristic knowledge to guide search

---

## 14. Uninformed Search Algorithms

| Algorithm                | Description                                                                                   | Completeness | Optimality | Time Complexity | Space Complexity |
|--------------------------|-----------------------------------------------------------------------------------------------|--------------|------------|----------------|-----------------|
| **Breadth-First Search**  | Expands shallowest nodes first; uses queue                                                    | Yes          | Yes        | O(b^d)         | O(b^d)          |
| **Depth-First Search**    | Explores deepest nodes first; uses stack                                                      | No           | No         | O(b^m)         | O(b*m)          |
| **Depth-Limited Search**  | DFS with depth cutoff limit; solves infinite path problem                                   | No           | No         | O(b^l)         | O(b*l)          |
| **Iterative Deepening DFS** | Combination of BFS and DFS; progressively increases depth limit                             | Yes          | Yes        | O(b^d)         | O(b*d)          |
| **Uniform-Cost Search**   | Expands node with lowest path cost; uses priority queue                                      | Yes          | Yes        | Depends on cost | Depends on cost |
| **Bidirectional Search**  | Runs two simultaneous searches – one forward from start and one backward from goal           | Yes          | Yes        | O(b^(d/2))     | O(b^(d/2))      |

---

## 15. Summary of Important Java Code Concepts

### Agent Cycle (Pseudocode)

```
while(true) {
    Percept percept = agent.getPercept();
    action = agent.program(percept);
    agent.performAction(action);
}
```

---

## End of Unit 1 Notes

---

**Good luck with your exam preparation!**  
The above material covers all essential theory, concepts, and typical exam questions with clear structure and examples.
```

