WorldSimulation 🌍

A Python project exploring population dynamics and social simulation.

The idea is to create a virtual population, define the rules governing its evolution, and observe the results over time.

The long-term goal is to build a world whose evolution emerges from the interactions between its inhabitants and the systems surrounding them.

«Create the rules. Run the simulation. Discover what happens.»

Current Version: V1

V1 establishes the foundations of the simulation.

It introduces individual citizens, a time system, and several social and economic mechanisms that affect the population.

👤 Citizens

Each citizen is represented by a Python "Citizen" object.

Citizens have individual attributes:

- Age and sex
- Money and salary
- Employment status
- Housing status
- Happiness
- Partner and family relationships
- Pregnancy status

⏳ Time

The simulation progresses month by month.

Time can be advanced manually:

Key| Action
"1"| +1 month
"2"| +3 months
"Shift"| +1 year
"Tab"| +3 years

💼 Employment

Citizens can be employed, unemployed or retired.

Employment changes according to predefined probabilities. Citizens can find jobs or lose their current employment.

Retirement begins at age 60.

💰 Economy

The economic system handles:

- Monthly salaries
- Food expenses
- Rent payments
- Income taxes
- Individual money balances

🏠 Housing

Citizens must pay rent to maintain their housing.

Repeated failure to pay rent can result in eviction and homelessness.

Housing conditions also influence happiness.

💀 Mortality

Citizens have age-dependent probabilities of dying.

Dead citizens remain recorded in the simulation so population history can be preserved.

❤️ Relationships and Reproduction

The simulation includes:

- Partnerships
- Partner relationships
- Pregnancy
- A nine-month pregnancy period
- Births
- Parent-child relationships

😊 Happiness

Each living citizen has a happiness score influenced by economic and personal conditions, including money, salary, housing and family relationships.

📊 Statistics

The simulation can display population indicators such as:

- Living and deceased population
- Average age
- Employment and unemployment
- Retirement
- Homelessness
- Average salary
- Age distribution

---

Architecture

WorldSimulation/
├── citizen.py
├── rules.py
├── simulation.py
└── main.py

- "citizen.py": citizen data and individual attributes.
- "rules.py": probabilities and simulation parameters.
- "simulation.py": world systems and time progression.
- "main.py": interface and user interaction.

---

Development Philosophy

WorldSimulation is also a learning project.

I want to understand every system I build rather than blindly adding features.

My development philosophy:

Understand → Build → Test → Improve → Repeat.

The project is developed progressively, with each system building upon the previous ones.

Long-Term Vision

V1 is only the foundation.

The ultimate ambition is to create a population whose collective evolution can produce unexpected outcomes.

Future development may include:

- More complex economic systems
- Individual decision-making
- More detailed social interactions
- Education and healthcare
- Politics and crime
- Social classes
- Migration
- Cities and communities
- More complex population dynamics

The goal is not to script every event.

It is to create rules and systems that interact, allowing unexpected situations and large-scale changes to emerge.

I want to be able to observe the population, understand what is happening, and sometimes intervene in the simulation.

Status

🟢 V1 — Foundation implemented

🚧 Future systems — Planned

---

WorldSimulation is a sandbox for experimenting with the evolution of a virtual society.
