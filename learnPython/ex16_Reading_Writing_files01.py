# -*- coding: utf-8 -*-
# Created on July 29th
# Felix Guerrero
# Exercise 16 - Reading and Writing Files  - Learn python the hard way.

# Import module sys
# Use ARGV package
from sys import argv

# Create variable Script from argv[0]
# Create variable filename from argv[1]
script, filename = argv

# Print out a description and insert variable filename
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

# Opening file
print "Opening the file..."
target = open(filename, 'w')

# Truncate the file
print "Truncating the file. Goodbye!"
target.truncate()

# Allow user to input string into three
# different variables, line1 - 3
print "Now I am going to ask you for three lines."
line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I am going to write these to the file."

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "and now we close it."
target.close()

