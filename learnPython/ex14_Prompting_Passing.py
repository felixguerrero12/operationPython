# -*- coding: utf-8 -*-
# Created on July 27th
# Felix Guerrero
# Exercise 14 - Prompting and Passing  - Learn python the hard way

#Importing Module
from sys import argv

script, user_name = argv

#Initiating Variable Prompt
prompt = '> '

#Print  Variable
print "Hi %s, I'm the %s script." % (script, user_name)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

# Creating variable using user interaction #2
print "Where do you live %s?" % user_name
lives = raw_input(prompt)

# Creating variable using user interaction #3
print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have %r computer. Nice.
""" % (likes, lives, computer)
