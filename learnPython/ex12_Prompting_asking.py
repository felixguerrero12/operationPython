# -*- coding: utf-8 -*-
# Created on July 27th
# Felix Guerrero
# Exercise 12 - Prompting  - Learn python the hard way.

#Creating Variables with Direct Raw_Input
age = raw_input("How old are you? \n")
height = raw_input("How tall are you? \n")
weight = raw_input("How much do you weight? \n")

# Print Variables
print "So, you are %r old, you are %r tall, and weight %r pounds."  % (age, height, weight)
