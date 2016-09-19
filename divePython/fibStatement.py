from sys import argv
n = argv[1]

def fib(n):
 print 'n =', n
 if n > 1:
   return n * fib(n-1)
 else:
   print 'end of the line'
   return 1
