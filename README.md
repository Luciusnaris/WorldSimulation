# WorldSimulation 🌍

A Python simulation project inspired by **BitLife**, **WorldBox**, and the idea of a small virtual world that can evolve over time.

The goal is simple: create a world populated by citizens, give them rules and systems, then observe what happens.

I want to eventually be able to sit back and watch my digital civilization completely fuck itself up. 🗿

---

## Why I Restarted the Project

My first version of WorldSimulation became too complicated too quickly.

I was learning Python while building the simulation, and I kept adding systems without really understanding how everything was connected. The result was messy, difficult to maintain, and increasingly difficult for me to understand.

So I decided to restart from scratch.

This time, I want to build the simulation progressively and understand every part of it before moving on.

The philosophy is:

> **Understand → Build → Test → Improve → Repeat.**

---

# V1

V1 is the first complete foundation of WorldSimulation.

The simulation contains a population of citizens living inside a small virtual world. Each citizen has their own characteristics and can interact with different systems that affect their life.

The world progresses month by month, with different systems being processed as time advances.

---

## Features

### 👤 Citizens

Each citizen has their own:

- Age
- Sex
- Money
- Salary
- Employment status
- Housing status
- Happiness
- Partner
- Parents
- Children
- Pregnancy

Citizens are individual objects created using the `Citizen` class.

---

### ⏳ Time

The simulation is based on months and years.

Citizens age as time passes, and different events are processed every month.

Time can currently be advanced manually:

| Key     | Action    |
| ------- | --------- |
| `1`     | +1 month  |
| `2`     | +3 months |
| `Shift` | +1 year   |
| `Tab`   | +3 years  |

Manual time progression makes it easier to test and observe the simulation.

---

### 💼 Employment

Citizens can be:

- Employed
- Unemployed
- Retired

Citizens have a probability of finding a job based on their age.

Employed citizens can also lose their jobs.

This means employment can change over time:

**Work → Lose job → Unemployment → Find another job**

Citizens retire at **60**.

---

### 💰 Economy

Citizens have their own money and salary.

Every month:

- Employed citizens receive their salary
- Citizens spend money on food
- Citizens have to pay rent
- Income taxes are applied

Money therefore changes continuously instead of simply accumulating forever.

---

### 🏠 Housing

Citizens have a housing status.

They must be able to pay their rent each month.

If they cannot pay rent for several consecutive months, they can lose their housing and become homeless.

Housing also affects citizen happiness.

---

### 💀 Death

Citizens have an age-based probability of dying.

The probability changes depending on their age, with older citizens generally having a higher probability of death.

When a citizen dies:

- Their state becomes `Dead`
- Their money becomes `0`
- Their salary becomes `0`
- Their happiness becomes `0`

Dead citizens remain in the simulation so the population history can still be observed.

---

### ❤️ Relationships

Adult citizens can automatically form partnerships.

Partners are linked to each other, meaning each citizen can reference their partner.

If a citizen's partner dies, the relationship is removed.

---

### 👶 Reproduction

Citizens can have children.

The reproduction system includes:

- Age-based birth probabilities
- Pregnancy
- A 9-month pregnancy period
- Parent/child relationships
- Money influencing birth probability

Children are added to the population as new citizens.

---

### 😊 Happiness

Each living citizen has a happiness percentage.

Happiness is calculated from several factors:

- Money
- Salary
- Housing
- Partner
- Children

Different factors contribute different amounts to the final happiness score.

Happiness can reach a maximum of **98%**, meaning a citizen can never reach 100% happiness.

---

### 📊 Population Statistics

The simulation can calculate information about the population, including:

- Living population
- Dead population
- Average age
- Employment rate
- Unemployment rate
- Retirement rate
- Homelessness rate
- Average salary
- Number of seniors
- Number of adults
- Number of minors

Detailed statistics can be displayed manually.

---

# Project Structure

```text
WorldSimulation/
│
├── citizen.py
├── rules.py
├── simulation.py
└── main.py


# 📁 Project Structure

The project is divided into four main files, each with a specific responsibility.

## `citizen.py`

Contains the `Citizen` class and the individual data and behaviour of citizens.

## `rules.py`

Contains the rules and probabilities used by the simulation:

- Death probabilities
- Job finding probabilities
- Job loss probabilities
- Birth probabilities
- Income tax
- Housing costs

## `simulation.py`

Contains the world itself and the systems that make it evolve:

- Time progression
- Death
- Employment
- Economy
- Taxes
- Housing
- Relationships
- Reproduction
- Happiness
- Population statistics

## `main.py`

Handles the user interface, keyboard controls and information displayed to the user.

---

# 🧠 What I Am Learning

WorldSimulation is also my way of learning Python by building something bigger than the individual concepts I am studying.

Through this project, I am learning:

- Object-oriented programming
- Classes and objects
- Composition
- Lists and dictionaries
- Functions
- Loops
- Randomization
- State management
- Debugging
- Git & GitHub
- Project organization
- Simulation logic

I am deliberately trying not to blindly vibe-code the project.

I want to understand the code I write and know why every part exists.

---

# 🧭 Philosophy

WorldSimulation is not supposed to be a perfect simulation of reality.

It is a sandbox.

I create rules, let them interact, and observe what happens.

Eventually, I want the world to become complex enough that I can introduce a new rule and have no idea exactly what will happen.

That's where the fun begins.

> **Understand → Build → Test → Improve → Repeat.**

---

# 🔮 Future Ideas

V1 is only the foundation.

Future versions may introduce systems such as:

- More complex economic behaviour
- More professions
- Different types of citizens
- More detailed relationships and families
- Education
- Health
- Crime
- Politics
- Culture
- More detailed life events
- Social classes
- Migration
- Cities
- More complex population dynamics
- Other systems that emerge naturally as the simulation develops

I don't want to add mechanics just because they sound cool.

The goal is to build systems that interact with each other and gradually create a more complex world.

---

# 🚧 Status

🟢 **V1 — Complete**

🚧 **Active development**
```
