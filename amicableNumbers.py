import math
def d(n):
    arrFactors =[]
    arrFactors.append(1)
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            arrFactors.append(i)
            if (n/i) not in arrFactors:
                arrFactors.append(n/i)
    return arrFactors

i =2
amicables =[]
while i<10000:
    arr = d(i)
    sum1 = reduce(lambda accum,element : accum + element, arr ,0);
    arr2 = d(sum1)
    sum2 = reduce(lambda accum, element: accum + element, arr2,0)
    if sum1 != i:
        if sum2==i:
            print "d(%d)= %d , and d(%d)=%d" % (i,sum1,sum1,i)
            print "\t factors of %d are %r , and factors of %i are %r" % (i,d(i),sum1,d(sum1))
            if i not in amicables:
                amicables.append(i)
            if sum1 not in amicables:
                amicables.append(sum1)
    i+=1

print amicables

sum3 = reduce(lambda accum, element : accum + element,amicables,0)
print "The sum of amicables under 10000 is: %d" % sum3
