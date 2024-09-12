# -*- coding: utf-8 -*-
"""CSST-101-MANGULABNAN-MP2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ksE69DDxH6OLKqeR7d3BO7tVURU1j3ON
"""

# p is the first boolean value and q is the second boolean value

# This perform the AND operation

def and_operation(p, q):
    return p and q

# This perform the OR operation

def or_operation(p, q):
    return p or q

# This perform the NOT operation

def not_operation(p):
    return not p


# This perform the IMPLIES operation

def implies_operation(p, q):
    return not p or q

# This determine the best action based on the current state
# Define the condition based on the state
def action(state):
  lowhealth = state['health'] <= 50
  enemy = state['distance'] <= 10
  power = state['power']

# This is the decision making logic
  if and_operation(lowhealth, enemy):
    return "Retreat"
  elif power:
    return "Use power"
  elif or_operation(lowhealth, enemy):
    return "Defend"
  else:
    return "Attack"

# Define sample state
state = {'health': 45, 'distance': 5, 'power': True}
# Determine and print the action based on the state
action = action(state)
print("The action is:", action)