# -*- coding: utf-8 -*-
# Created on July 29th
# Felix Guerrero
# Exercise 18 - Names, Variables, Code, Functions  - Learn python the hard way.

# This one is like your scripts with argv
def print_two(*args):
 arg1, arg2 = args
 print "arg1: %r, arg2: %r" % (arg1, arg2)

# Okay, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
 print "arg1: %r, arg2: %r" % (arg1, arg2)

# This just takes one arguement
def print_one(arg1):
 print "arg1: %r" % arg1

# This one takes no arguments
def print_none():
 print "I got nothin'."

# Insert data into the definitions
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

