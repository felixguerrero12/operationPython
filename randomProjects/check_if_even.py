# This program allows you to check if your input is even.

i = int(raw_input("Enter to check if the number is odd or even: "))
if i % 2 == 0:
	print "The number: %d is even." % i
else:
	print "The number: %d is odd." % i
