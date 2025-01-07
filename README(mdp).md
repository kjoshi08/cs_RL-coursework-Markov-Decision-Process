
# Markov Decision Process (MDP) Quiz - AI with Reinforcement Learning

## Overview

This repository contains the solution to a Markov Decision Process (MDP) problem from the quiz. The task involves computing the optimum state-value functions and policy for an MDP with three states: Starve, Hungry, and Full. The discount factor (gamma) is set to 0.9, and the solution also includes Python code for iterating the computations and tweaking the gamma value.

---

## Problem Description

### States and Actions:
1. **States**: 
   - Starve (Terminal State)
   - Hungry
   - Full
2. **Actions**: 
   - `Eat`
   - `Don’t Eat`

### Goal:
1. Compute the **optimal state-value functions** for all states.
2. Derive the **optimal policy** for the given MDP.

### Assumptions:
- The discount factor, gamma (\(\gamma\)), is set to 0.9.

---

## Methodology

### 1. State-Value Function Computation:
The Bellman equation is used to calculate the state values iteratively:
\[ V(s) = \max_a \sum_{s'} P(s'|s,a) \left[ R(s,a,s') + \gamma V(s') \right] \]

### 2. Optimum Policy Computation:
The policy is derived by selecting actions that maximize the state values:
- For the Hungry state, compare `Eat` vs `Don’t Eat`.
- For the Full state, only `Don’t Eat` is available.
- The Starve state is terminal.

---

## Results

### Final State Values:
- **Starve**: -10 (fixed)
- **Hungry**: 1.16
- **Full**: 0.36

### Optimal Policy:
- **Hungry**: `Eat`
- **Full**: `Don’t Eat`
- **Starve**: No action (terminal state)

---

## Python Implementation

The provided Python script iteratively computes the state values and determines the optimal policy. It allows for tweaking the discount factor (\(\gamma\)) and includes convergence checks.

---
