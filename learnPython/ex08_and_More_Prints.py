# -*- coding: utf-8 -*-
# Created on July 27th
# Felix Guerrero
# Exercise 8 - Printing and Printing  - Learn python the hard way.

#Creating Variable
formatter = "%r %r %r %r"

# Printing Formatter
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)

print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
