# -*- coding: utf-8 -*-
# Created on July 29th
# Felix Guerrero
# Exercise 17 - More Files  - Learn python the hard way.

# Import argv from sys package
# Import exists from os.path
from sys import argv; open(argv[2], 'w').write(open(argv[1]).read())


# Use three arguements as these variables
# script, from_file, to_file = argv

# Redundent
# print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
#  in_file = open(from_file)
#  indata = in_file.read()
# Converted code into one line :
# with open(from_file) as fp: indata = fp.read()

# print "The input file is %d bytes long" % len(indata)
# print "Does the output file exist? %r" % exists(to_file)
# raw_input()

# convert two lines of code into one
# with open(to_file, 'w') as tf: out_file = tf.write(indata)

# out_file = open(to_file, 'w')
# out_file.write(indata)

# print "Alright, all done."

# out_file.close()
# in_file.close()
