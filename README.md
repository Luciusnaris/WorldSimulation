# WorldSimulation 🌍

WorldSimulation is a Python simulation project inspired by games like **BitLife** and **WorldBox**.

The idea is to create a small simulated world where citizens have their own attributes and behaviors, then gradually add systems that make the world evolve over time.

The long-term goal is to be able to observe the population, introduce new rules, and see how the world reacts to them.

---

## 🚧 Why I restarted the project

This project did not start with the structure it has today.

My first version became more complicated than I could properly manage. I was learning new Python concepts while trying to build a simulation that was already becoming too ambitious.

I was adding features faster than I was organizing the project.

Eventually, I decided to **restart WorldSimulation from scratch** instead of continuing to build on top of code I no longer fully understood.

This time, I wanted to take a slower approach:

> **Build one mechanic, understand it, test it, then move on to the next one.**

The current version is therefore not just a new version of the simulation. It is also a new approach to how I develop the project.

---

# 📈 Development Progress

## V0.1 — The Beginning

The first goal was extremely simple: create citizens.

I created a `Citizen` class containing basic information about each citizen.

### Added

* `Citizen` class
* Random citizen ages
* Random starting money
* A list containing all citizens
* Generation of an initial population

At this stage, citizens were basically just data.

There was no concept of time or interaction between the different systems yet.

---

## V0.2 — Introducing Time

The next step was making the world actually move forward.

I introduced a basic time system using **months and years**.

### Added

* `month` variable
* `year` variable
* `advance_time()` function
* Automatic aging every 12 months
* `age_up()` method for individual citizens

The important design decision here was separating **world mechanics** from **citizen mechanics**.

The world controls the passage of time, while each citizen is responsible for changing their own age.

---

## V0.3 — Salaries

After having time progression, I needed something that could happen during that time.

I added employment-related income.

Citizens can now have an individual salary, which is generated when they are created.

### Added

* Individual salaries
* Random salary generation
* Monthly salary payments
* Salary stored as a citizen attribute

This introduced the first real economic system into the simulation.

---

## V0.4 — Spending

Having citizens earn money without ever spending it obviously wouldn't make for a very interesting economy.

So I added monthly spending.

Each month, a citizen spends a random percentage of their current money.

### Added

* Monthly spending
* Random spending between 10% and 50% of current money
* Spending based on current wealth rather than salary

Using current money instead of salary was intentional because future citizens may not have a salary at all.

---

## V0.5 — Employment, Unemployment & Retirement

The next step was making employment less binary.

Not every citizen should have a job.

I introduced employment probabilities and retirement.

### Added

* Employed citizens
* Unemployed citizens
* 70% employment probability for working-age citizens
* 30% unemployment probability
* Retirement at age 60
* Retired citizens have no salary

This was also the first step toward making citizens behave differently depending on their age.

---

## V0.6 — Automatic Simulation

Until this point, time had to be advanced manually.

I wanted to actually **watch the simulation run**.

I added an automatic time loop with different simulation speeds.

### Added

* Automatic monthly time progression
* Normal speed
* Fast speed
* Slow speed
* Pause functionality
* Resume functionality
* Keyboard controls
* Startup instructions
* 10-second startup countdown

### Controls

| Key | Action       |
| --- | ------------ |
| `1` | Normal speed |
| `2` | Fast speed   |
| `3` | Slow speed   |
| `0` | Pause        |

For now, the simulation uses **10 citizens** instead of 100.

This makes it easier to observe individual citizens and verify that the systems are actually working before increasing the population again.

---

# 🧠 What I am learning

WorldSimulation is also an experiment in learning how to build software properly.

Instead of trying to create the entire simulation at once, I am gradually learning how different systems interact:

* Object-oriented programming
* Classes and objects
* Inheritance, composition and polymorphism
* Randomized systems
* Time-based simulation
* State management
* Loops and conditional logic
* Basic simulation design
* Debugging and testing
* Git and GitHub
* Project organization

The project is intentionally being built step by step.

---

# 🤖 AI-Assisted Learning

I am building this project as a way to learn and improve my Python and software development skills.

I use AI as a **learning assistant and technical advisor**: to explain concepts, discuss design decisions, help debug problems, and challenge my reasoning.

The project is developed progressively, with the goal of understanding and writing the code myself rather than blindly generating it.

AI is there to help me understand the problem, not to build the entire project for me.

---

# 🛠️ Technologies

* Python
* Git
* GitHub

---

# 🔮 Future Ideas

There are many systems I would like to experiment with in the future.

Some possible ideas include:

* Population growth
* Reproduction
* Relationships
* Families
* Jobs and different professions
* More complex economies
* Happiness and mood
* Random events
* Diseases
* Crime
* Education
* Death
* Different social classes
* Government and laws
* Natural disasters
* Wars and conflicts
* Political systems
* Major world events

Some of these ideas may change completely as the project develops.

For now, the priority is to build a solid foundation before adding more complexity.

---

# 📌 Current Philosophy

WorldSimulation is not meant to be built as quickly as possible.

One of the biggest lessons from the first attempt was that **adding features faster does not necessarily mean making better progress**.

The current approach is simple:

**Understand → Build → Test → Improve → Repeat.**

The simulation may start small, but the goal is to gradually turn it into a living system where unexpected things can happen simply because different rules interact with each other.

I want to be able to define or change rules and then observe what happens instead of manually scripting every outcome.

And yes, eventually I want to be able to sit back and watch my little digital civilization completely fuck itself up. 🗿

---

## 📊 Status

🚧 **Active development — V0.6 SOON V1**

The simulation is still in its early stages, but the foundation is being built progressively and deliberately.
