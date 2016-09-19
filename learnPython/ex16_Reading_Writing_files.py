# -*- coding: utf-8 -*-
# Created on July 27th
# Felix Guerrero
# Exercise 16 - Reading and Writing Files  - Learn python the hard way

#Import Sys Package and Import argurment module
from sys import argv

# Allow the variable script and filename to be entered through the commandline.
script, filename = argv

# Print couple of strings with variables
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want to do that, hit RETURN."

# A Way to verify if I want to delete the file.
raw_input("?")

#1. Print out that you are opening the file.
#2. Open file and give it to variable target.
print "Opening the file..."
target = open(filename, 'w')

#1. Print out that you are going to truncate a file.
#2. Truncate variable target.
print "Truncating the file. Say Goodbye."
target.truncate()

#1. Print output of you requesting for 3 lines.
#2. Three raw_input for three different variables.
print "Now, I am going to ask you for three lines."
#line1 = raw_input("Line 1: ")
#line2 = raw_input("Line 2: ")
#line3 = raw_input("Line 3: ")

# Print advising that I am going to write these lines to the target variable file.
# Three different target.write which are used to writing to the target.
print "Please write three lines:"
target.write(raw_input())
target.write(raw_input())
target.write(raw_input())
#target.write("\n")
#target.write(line3)
#target.write("\n")

# Print out the file we have just written.
#print target.read()

#1. Print advising the file will be closing.
#2. Close the file.
print "Closing the file."
target.close()

# Give Variable fileName the variable file filename.
fileName = open(filename)
print fileName.read()
