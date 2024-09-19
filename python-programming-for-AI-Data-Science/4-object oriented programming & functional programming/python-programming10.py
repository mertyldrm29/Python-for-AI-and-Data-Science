# Functional Programming in Python

# Pure Functions

# Example 1 - Independency

A = 9

def impure_sum(b):
    return b + A

def pure_sum(a,b):
    return a + b

impure_sum(6)
pure_sum(3, 4) # this function's output will always be 7, but the impure_sum's output
               # is depended to A

# Example 2 - Deadly Side Effects
# OOP

class LineCounter:
    def __init__(self,filename):
        self.file = open(filename,'r')
        self.lines = []
    
    def read(self):
        self.lines = [line for line in self.file]
    
    def count(self):
        return len(self.lines)
        
lc = LineCounter('demotext.txt')

print(lc.lines)
print(lc.count())

lc.read()

print(lc.lines)
print(lc.count())

# With Functional Programming

def read(filename):
    with open(filename,'r') as f:
        return [line for line in f]
    
def count(lines):
    return len(lines)

example_lines = read('demotext.txt')
lines_count = count(example_lines)
lines_count

# Anonymous Functions

def old_sum(a,b):
    return a+b
old_sum(4, 5)

new_sum = lambda a,b : a+b
new_sum(4,5)

unordered_list = [('b',3),('a',8),('d',12),('c',1)]
unordered_list

sorted(unordered_list, key = lambda x: x[1])
unordered_list

# vectorel operations
# OOP

a = [1,2,3,4]
b = [2,3,4,5]

ab = []

range(0,len(a))

for i in range(0,len(a)):
    ab.append(a[i]*b[i])

ab

# Functional Programming

import numpy as np
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])
a*b

# Map & Filter & Reduce

list1 = [1,2,3,4,5]

for i in list1:
    print(i+10)

list(map(lambda x: x*10, list1))

# filter

list2 = [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x: x % 2 == 0, list2)) # it's like using if 

# reduce

from functools import reduce

list3 = [1,2,3,4]
reduce(lambda a,b: a+b, list3)

# creating module

import CalculatorModule
CalculatorModule.new_salary(1000)
CalculatorModule.new_salary(2000)

import CalculatorModule as cm
cm.new_salary(1000)

from CalculatorModule import new_salary
new_salary(4000)

import CalculatorModule as cm
cm.salaries


# Errors / Exceptions

# ZeroDivisionError

a = 10
b = 0
a/b

try:
    print(a/b)
except ZeroDivisionError:
    print("No 0 in the denominator")
    
# Type Error

a= 10
b="2"
a/b

try:
    print(a/b)
except TypeError:
    print("Integer and String problem.")

