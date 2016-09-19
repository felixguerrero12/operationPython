# -*- coding: utf-8 -*-
# Created on July 29th
# Felix Guerrero
# Exercise 20 - Functions and Files  - Learn python the hard way.

# Import Module from package:
from sys import argv

# Create variable for input_file:
input_file = argv[1]

# Create a print all function:
def print_all(f):
 print f.read()

# Create a rewind function:
def rewind(f):
 f.seek(0)

# Create a print line function:
def print_a_line(line_count, f):
 print line_count, f.readline()

# Open input_file into variable current_file:
current_file = open(input_file)

# Description of what is going to happen
# Use function print_all inserting current_file
print "First let's print the whole file:\n"
print_all(current_file)

# Rewind the file back
# seek(0) reference point of the beginning of the file
print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines: "

# Current position in the file
# Read line in position one
current_line = 1
print_a_line(current_line, current_file)

# Current position plus 1
# Read line in position two
current_line = current_line + 1
print_a_line(current_line, current_file)

# Current position plus 1 more:
# Read line in position three
current_line = current_line + 1
print_a_line(current_line, current_file)
