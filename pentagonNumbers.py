import math

def isPentagonal(p):
    n = (1 + math.sqrt(1+24*p))/6
    if n - int(n) == 0:
        return True
    return False

def pn(a):
    return a*(3*a -1)/2
found = False
x = 2
while not found:
    for y in range(1,x):
        if isPentagonal(pn(x) -pn(y)) and isPentagonal(pn(y) + pn(x)):
            print x,y,pn(x),pn(y),pn(x)-pn(y)
            found = True
    x +=1
