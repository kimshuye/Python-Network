import socket
print (socket.gethostbyname(socket.gethostname()))

 # Module sys has to be imported:
import sys

# Iteration over all arguments:
for eachArg in sys.argv:
        print eachArg

def arithmetic_mean(x, *l):
    """ The function calculates the arithmetic mean of a non-empty
        arbitrary number of numbers """
    sum = x
    for i in l:
        sum += i

    return sum / (1.0 + len(l))

raw_input()