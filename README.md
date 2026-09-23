# WorldSimulation 🌍

A Python simulation project inspired by **BitLife**, **WorldBox**, and the idea of a small virtual world that can evolve over time.

The goal is simple: create a world populated by citizens, give them rules and systems, then observe what happens.

I want to eventually be able to sit back and watch my digital civilization completely fuck itself up. 🗿

---

## Why I restarted the project

My first version of WorldSimulation became too complicated too quickly.

I was learning Python while building the simulation, and I kept adding systems without really understanding how everything was connected. The result was messy, difficult to maintain, and increasingly difficult for me to understand.

So I decided to restart from scratch.

This time, I want to build the simulation progressively and understand every part of it before moving on.

The philosophy is:

**Understand → Build → Test → Improve → Repeat.**

---

# Development Progress

## V0.1 — The Beginning

The first version introduced the basic concept of citizens.

Each citizen had:

* An age
* Money
* A randomly generated starting state

I created a `Citizen` class and stored all citizens inside a list.

This was where I started getting more comfortable with:

* Classes
* Objects
* Lists
* Loops
* Random values
* Object attributes

---

## V0.2 — Time

I added the concept of time.

The simulation now has:

* Months
* Years
* Citizens aging over time

Instead of putting world time inside the `Citizen` class, I created a separate `advance_time()` function responsible for moving the world forward.

This helped me understand the difference between something that belongs to an individual citizen and something that affects the entire simulation.

---

## V0.3 — Salaries

Citizens can now have a salary.

Their salary is generated when they are created and remains part of their individual state.

Each month, employed citizens receive their salary.

This introduced the first real economic mechanic of the simulation.

---

## V0.4 — Spending

Citizens now spend money every month.

Their spending is based on their current amount of money, with a random percentage between 10% and 50%.

This means that citizens don't simply accumulate money forever.

The economy can now actually change over time.

---

## V0.5 — Employment, Unemployment & Retirement

Citizens can now be:

* Employed
* Unemployed
* Retired

When a citizen is created, there is a 70% chance of being employed and a 30% chance of being unemployed.

Citizens retire at 60 and stop receiving a salary.

This was another step toward making citizens behave differently from one another instead of being simple containers of random numbers.

---

## V0.6 — Automatic Time... Then I Changed My Mind

At first, I wanted the simulation to run automatically.

Until this point, time had to be advanced manually, so I added an automatic time loop with different simulation speeds.

The idea was to be able to simply sit back and watch the world evolve.

I added:

* Automatic monthly time progression
* Normal / fast / slow speeds
* Pause / resume
* Keyboard controls
* A startup countdown

However, after actually using it, I realized that **automatic time was a bad idea for the current stage of the project**.

While developing the simulation, I need to be able to control exactly when time passes. Automatically advancing the world made testing mechanics more annoying and made it harder to observe what was happening.

So I removed the automatic system.

Time is now advanced manually:

* `1` → +1 month
* `2` → +3 months
* `Shift` → +1 year
* `Tab` → +3 years

This ended up being a useful lesson: **a feature can sound good in theory but still be bad for the actual workflow of the project.**

---

## V0.7 — Death

The world is no longer populated by immortal citizens. 💀

Citizens now have a probability of dying based on their age.

Older citizens have a significantly higher chance of dying than younger citizens.

When a citizen dies:

* Their state becomes `Dead`
* Their salary becomes `0`
* Their money becomes `0`
* Their happiness becomes `0`

The death system is based on probabilities defined separately from the simulation itself.

This introduced an important concept for the project:

**Rules determine what can happen. The simulation applies those rules to**
