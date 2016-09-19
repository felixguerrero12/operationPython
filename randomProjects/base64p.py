# Felix Guerrero
# July 27th, 2016
# Basic Python Decoder
import base64
import sys

coded_string = sys.argv[1]
print "Coded string: ", coded_string
decoded_string = coded_string.decode('base64')
print "Decoded string: ", decoded_string
