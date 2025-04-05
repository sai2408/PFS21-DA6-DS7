import math
def factorial(a):
    print(math.factorial(a))
def primeornot(a):
    fc = 0
    for i in range(1,a+1):
        if a%i==0:
            fc = fc + 1
    if fc == 2:
        print(True)
    else:
        print(False)
def reverse(a):
    if a >= 0:
        x = str(a)
        return x[::-1]
    else:
        a = abs(a)
        x = str(a)
        r = "-" + x[::-1]
        return r
        
