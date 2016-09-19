# -*- coding: utf-8 -*-
# Created on July 26th
# Felix Guerrero
# Exercise 5 - More variables and printing  - Learn python the hard way.

#Defining Variables
name = 'Felix R. Guerrero'
age = 23 # Current age
height = 70.0 # Height in inches
weight = 185.0 # In pounds
eyes = 'brown'
teeth = 'white'
hair = 'brown'

#Printing out
print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair) # Double variable insertion.
print "His are usually %s depending on the coffee." % teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight,  age + height + weight)

#Converting the weight from pounds to kilograms
print "The weight in kilograms is %r." % (weight * 0.453592)

#Converting the height from inches to centimeters
print "The height in centimeters is %r." % (height * 2.54)

#Comments
# To replace all my_ with blank spaces do
# :s/my_/g
#
# 1 inch = 2.54 centimeters
# 1 pound = 0.453592 Kilograms
