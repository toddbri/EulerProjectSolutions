

def divide(n,d):
    # print "dividing %d by %d " % (n,d)
    global repeat
    global remainders
    global result
    global repeatLength
    global repeatPositions
    numerator = n
    if not numerator in remainders:
        remainders.append(numerator)
        repeatPositions.append(repeat)
    else:
        sundry = remainders.index(numerator)
        repeatLength= repeat - sundry
        return
    numerator *= 10
    while numerator < d:
        numerator *= 10
        result += "0"
        repeat +=1
        if not numerator in remainders:
            remainders.append(numerator)
            repeatPositions.append(repeat)
        else:
            sundry = remainders.index(numerator)
            repeatLength= repeat - sundry
            return
    remainder = numerator % d
    result +=str(int(numerator/d))
    if remainder == 0:
        return
    else:
        repeat +=1
        divide(remainder,d)



largest = 0
number = 0
longestresult = 0

for i in range(2,1001):
    print "dividing %d into 1" % i
    repeatLength = 0
    repeat = 0
    remainders = []
    repeatPositions =[]
    result = "0."
    divide(1,i)
    if repeatLength > largest:
        largest = repeatLength
        number = i
        longestresult = result
    print "\trepeat: ", repeat
    print "\trepeat length: ", repeatLength
    print "\tremainders: " , remainders
    print "\trepeat positions: ", repeatPositions
    print "\tresult: ", result

print "*" * 10
print "the number: ", number
print "has the longest repeat pattern of: " , largest
print "with a result of: " , longestresult
