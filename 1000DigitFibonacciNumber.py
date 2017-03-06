
found = False
counter = 1
a = 0
b = 1
while not found:
    a,b = b, a+b
    counter +=1
    if len(str(b))==1000:
        found = True
        print "fib(%d) = %d" % (counter, b)
