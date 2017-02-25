a = 0
found = False
while not found:
    a +=1
    for b in range(a+1,1000-a):
        c = 1000-a-b
        if ((a**2 + b**2)==c**2):
            print "a: %d, b: %d, c: %d" % (a,b,c)
            found = True
        if found:
            break

print "a*b*c = %d" % (a*b*c)
