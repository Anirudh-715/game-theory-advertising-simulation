# Game Theory Simulation of Advertising Competition

## Research Question

How do different strategic behaviors affect profits in repeated advertising competition between firms?

This project investigates whether cooperative strategies (avoiding advertising) can outperform aggressive strategies (always advertising) in repeated interactions.

## Key Findings

From the simulations:

- Firms that always advertise can exploit firms that never advertise.
- However, cooperative strategies such as Tit-for-Tat can stabilize mutually beneficial outcomes.
- When both firms constantly advertise, profits decrease due to advertising costs.

These results illustrate the strategic tension described in the Prisoner's Dilemma and demonstrate how repeated interactions influence economic decision-making.

## Introduction

In many markets, firms compete by investing in advertising to attract customers.
However, when competing firms continuously advertise, the overall profit of both firms may decrease due to high advertising costs.

This situation can be modeled using the **Prisoner's Dilemma** from game theory.
Each firm must decide whether to **advertise** or **not advertise**, while the outcome depends on the decision made by the competing firm.

This project simulates advertising competition between firms using a repeated Prisoner's Dilemma model.

---

## Economic Motivation

In oligopolistic markets, firms often face strategic decisions where their optimal action depends on the choices of competitors.

For example:

* If both firms avoid advertising, they save costs and earn higher profits.
* If one firm advertises while the other does not, the advertising firm gains a competitive advantage.
* If both firms advertise, both incur high costs and profits decrease.

This leads to a strategic dilemma where rational firms may choose strategies that produce worse outcomes for everyone.

---

## Payoff Structure

The simulation uses the following payoff matrix:

| Firm A | Firm B | Profit A | Profit B |
| ------ | ------ | -------- | -------- |
| NoAd   | NoAd   | 10       | 10       |
| Ad     | NoAd   | 15       | 2        |
| NoAd   | Ad     | 2        | 15       |
| Ad     | Ad     | 5        | 5        |

Interpretation:

* Mutual cooperation (NoAd, NoAd) gives both firms high profit.
* If one firm advertises while the other does not, the advertiser benefits.
* If both advertise, profits are lower due to advertising costs.

---

## Strategies Implemented

The simulation compares different strategic behaviors:

### Always Advertise

The firm advertises in every round regardless of the opponent’s action.

### Never Advertise

The firm never advertises and always cooperates.

### Tit-for-Tat

The firm starts by not advertising and then copies the opponent's previous action.

This strategy is widely studied in repeated game theory models.

---

## Experimental Setup

The program simulates repeated interactions between firms.

* Number of rounds: 100
* Firms use predefined strategies
* Each round calculates profits using the payoff matrix

The total profit accumulated by each strategy is recorded and compared.

---

## Example Output

Example result from the simulation:

AlwaysAd vs NeverAd -> (1500, 200)
AlwaysAd vs TitForTat -> (500, 500)
NeverAd vs TitForTat -> (1000, 1000)

These results demonstrate how different strategies perform in repeated strategic interactions.

---

## Visualization

The simulation results are visualized using bar graphs to compare the
profit outcomes of different strategy matchups.

<p align="center">
  <img src="image_2026-03-12_182445032..png" width="600">
</p>

## Technologies Used

Python

---



---

## Future Work

Possible improvements include:

* Adding more strategies (Grim Trigger, Random Strategy)
* Simulating multiple competing firms
* Visualizing results using graphs
* Modeling other economic scenarios such as cartel pricing or price competition


