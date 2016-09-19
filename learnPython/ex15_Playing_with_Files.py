# -*- coding: utf-8 -*-
# Created on July 27th
# Felix Guerrero
# Exercise 15 - Playing with Files  - Learn python the hard way.

# This uses the sys package and imports the arguements module.
from sys import argv

#Allow the variable script and filename to be entered through the commandline.
script, filename = argv

# Insert the filename content to variable txt.
# Create a file object.
txt = open(filename)

# Telling you what filename has been entered.
print "Here is your file name: %r" % filename

#Print the content of the file
#txt.read() - This outputs the content of the variable txt.
print txt.read()
txt.close()

## Requests for enterting variable file_name.
#print "Type the filename again:"
#file_again = raw_input("> ")

## Give variable file_again content to txt_again.
#txt_again = open(file_again)

# Printout the content of variable txt_again.
#print txt_again.read()

