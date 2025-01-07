import numpy as np


# Define the states
states = ['Starve', 'Hungry', 'Full']


# Initialize values for each state
V = {'Starve': -10, 'Hungry': 0, 'Full': 0}
gamma = 0.9
theta = 1e-5  # convergence threshold


# Transition probabilities and rewards
def transition(state, action, V, gamma):
    if state == 'Full':
        if action == 'Don’t Eat':
            return 0.5 * (1 + gamma * V['Full']) + 0.5 * (-1 + gamma * V['Hungry'])
    elif state == 'Hungry':
        if action == 'Eat':
            return 0.9 * (1 + gamma * V['Full']) + 0.1 * (-1 + gamma * V['Hungry'])
        elif action == 'Don’t Eat':
            return 0.9 * (-10 + gamma * V['Starve']) + 0.1 * (-1 + gamma * V['Hungry'])
    return 0


def policy_iteration(V, gamma, theta):
    delta = float('inf')
    while delta > theta:
        delta = 0
        V_new = V.copy()
        for state in V:
            if state == 'Starve':
                continue
            if state == 'Full':
                V_new[state] = transition(state, 'Don’t Eat', V, gamma)
            elif state == 'Hungry':
                V_new[state] = max(transition(state, 'Eat', V, gamma), transition(state, 'Don’t Eat', V, gamma))
            delta = max(delta, abs(V_new[state] - V[state]))
        V = V_new
    return V


# Compute the optimal values
V_optimal = policy_iteration(V, gamma, theta)
print("Optimal State Values:", V_optimal)


# Derive the optimal policy based on state values
def optimal_policy(V, gamma):
    policy = {}
    policy['Hungry'] = 'Eat' if transition('Hungry', 'Eat', V, gamma) > transition('Hungry', 'Don’t Eat', V, gamma) else 'Don’t Eat'
    policy['Full'] = 'Don’t Eat'  # Only action available
    return policy


# Compute the optimal policy
policy = optimal_policy(V_optimal, gamma)
print("Optimal Policy:", policy)