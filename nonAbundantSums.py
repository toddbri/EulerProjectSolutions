import math
def d(n):                           # d(n) returns an array of all proper factors of n
    arrFactors =[]
    arrFactors.append(1)
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            arrFactors.append(i)
            if (n/i) not in arrFactors:
                arrFactors.append(n/i)
    return arrFactors

abundants = []
for i in range(1,28124):
    sumFactors = reduce(lambda accum, element : accum + element,d(i),0)
    if sumFactors > i:
        abundants.append(i)
        # print i, d(i), sumFactors
print "%d abundants found." % len(abundants)
targetInts =[]
for i in range(1,28124):
    targetfound = False
    for a in abundants:
        if a>i:
            break
        for b in abundants:
            if a+b>i:
                break
            if i == (a+b):
                targetfound = True
                break
        if targetfound:
            break
    if not targetfound:
        targetInts.append(i)
    print "i: ", i
    print "%d target Integers found." % len(targetInts)
    # print targetInts
print targetInts
sum = reduce(lambda accum,element : accum + element,targetInts,0)
print sum
