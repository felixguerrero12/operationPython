# -*- coding: utf-8 -*-
# Created on July 27th
# Felix Guerrero
# Exercise 16a - This is used to read a file  - Learn python the hard way.
from sys import argv
filename = argv[1]
txt = open(filename)
print txt.read()
