# -*- coding: utf-8 -*-
"""CSST-101-MANGULABNAN-MP2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ksE69DDxH6OLKqeR7d3BO7tVURU1j3ON
"""

# Evaluate if the predicate holds true for all element in the domain


def forall(predicate, domain):
  return all(predicate(element) for element in domain)


# Evaluate if the predicate holds true for at least one element in the domain


def exist(predicate, domain):
  return any(predicate(element) for element in domain)

# defining the domain of elements

domain = [1, 2, 3, 4, 5]

def even(x):
# Predicate function checking if the number is even
  return x % 2 == 0

print(forall(even, domain))
print(exist(even, domain))