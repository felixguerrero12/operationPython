# This uses the sys module and imports the arguements feature.
from sys import argv
script, filename = argv

txt = open(filename)
print "The output of your file : %r" % filename
print "\nOutput:\n"
print txt.read()

