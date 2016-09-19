# -*- coding: utf-8 -*-
# Created on July 26th
# Felix Guerrero
# Exercise 6 - Strings and text  - Learn python the hard way.

#Variables
x = "There are %d types of people." %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

#Print Variables
print x
print y


#Print Strings
print "I said: %r." % x
print "I also said: '%s'." % y

#Setting Variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Print String with Raw Variable
print joke_evaluation % hilarious

# Setting Variable W and E
w = "This is the left side of..."
e = "a string with a right side."

print w + e
