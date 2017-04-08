factorials = [1,1,2,6,24,120,720,5040,40320,362880]

for i in range(10,2540160):
    stri = str(i)
    sum = 0
    # print "i: ",i
    for j in range(0,len(stri)):
        # print 'checking: ', stri[j]
        # print factorials[int(stri[j])]
        sum += factorials[int(stri[j])]
        if sum == i:
            print i
