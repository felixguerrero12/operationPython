# -*- coding: utf-8 -*-
# Created on July 29th
# Felix Guerrero
# Exercise 21 - Functions can return something  - Learn python the hard way.

# Create a addition function using a and b
# Return the addition of a + b
def add(a, b):
 print "Adding %d plus %d" % (a, b)
 return a + b

# Create a subtracting function using a and b
# Return the subtracting of a - b
def subtract(a, b):
 print "Subtracting %d - %d" % (a, b)
 return a - b

# Create a multiplication function using a and b
# Return the multiplication of a and b
def multiply(a, b):
 print "Mutiplying %d * %d" % (a, b)
 return a * b

# Create a division function using a and b
# Return the division of a and b
def divide(a, b):
 print "Dividing %d / %d" % (a, b)
 return a / b


print "Let's do some math with just functions !"

# Creating the variables:
# Variables creation
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100,2)

# Print the variables in this format:
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A Puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

# 1. Divide IQ by 2, IQ before entering function is 50
# 1a. Variable a is 50. Variable b is 2.
# 1b. 50 / 2 = 25

# 2. Multiply weight by variable b. Variable a = 25
# 2a. Weight or Variable b is 180.
# 2b. 180 * 25 = 4500

# 3. Subtract height by variable b.
# 3a. Variable a is 74. Variable b is 4500.
# 3b. 74 - 4500 = -4426

# 4. Add age by variable b.
# 4a. Variable a is 35. Variable b is -4188
# 4b. 35 + -4426 = -4391

what = add(age, subtract(height, multiply(weight, divide(iq,2))))
print "That becomes: ", what, "Can you do it by hand?"

inverse_what = divide(iq, multiply(weight, subtract(height, add(age,6000))))
print "The inverse becomes: ", inverse_what
