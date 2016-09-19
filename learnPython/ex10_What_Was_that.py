# -*- coding: utf-8 -*-
# Created on July 27th
# Felix Guerrero
# Exercise 10 - What was that?  - Learn python the hard way.

# Creating Variables
tabby_cat = "\tI'm tabbed in.\n"
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."

# Creating Fat Cat Variable
fat_cat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# Print all Variables
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# While LOOP : Spinning bar
while True:
	for i in ["/", "-", ",", "|", "\\", "|"]:
		print "%s\r" % i,
