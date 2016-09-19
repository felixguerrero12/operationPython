# Felix Guerrero
# Example 15 - Reading Files
# June 28th, 2016

# Import the sys package and import the arguement module
from sys import argv

# The first two command line arguements in the variable will be
# these variables
script, filename = argv

# 1. Open up variable filename
# 2. Give the content of the file to txt
txt = open(filename)

# 1. Print the Variable Filename
# 2. Read the variable txt
print "Here's your file %r" % filename
print txt.read()

# 1. Print the variable filename again:"
# but with a different format instead.
print "Type the filename again:"
file_again = raw_input("> ")

# 1. Open the file and give the content to variable txt_again
# 2. print txt_again.read()
txt_again = open(file_again)
print txt_again.read()
