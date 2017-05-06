
def isPentagonal(x):
    a = 1
    while pn(a) <= x:
        if pn(a) == x:
            return True
        a +=1
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
