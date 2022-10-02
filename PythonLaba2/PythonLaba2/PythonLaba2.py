'''
import math
import functions as f

def calc(m):
    d = 2
    while d <= math.sqrt(m) and m % d != 0:
        d += 1
    if d > math.sqrt(m) and m != 1:
        print(m, "is prime number!")	
    else:
        print(m, "is not prime number!")

n = int(input("Enter N "))
if n < 0:
    n = f.morethannull(n)
calc(n)
'''

def function(a):
    z = 1 / (a**(0.5) + 2**(0.5))
    return z 

def function2(a):
    while a < 0:
        a = int(input("Enter enother m, that is > 0!\n"))
    return a

m = int(input("Enter m "))
m = function2(m)
print("Result = ", function(m))




