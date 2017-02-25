found = False
i = 20
while not found:
    got_it=True
    for x in range(2,21):
        if (i%x != 0):
            got_it = False
    if got_it:
        found = True
    else:
        i+=1
print "smallest positive number that is evenly divisible by the numbers 1-20 is %d" %i
