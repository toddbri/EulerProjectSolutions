import math
def isPrime(value):
    isAPrime = True
    for x in range(2,int(math.sqrt(value)+1)):
        if value % x == 0:
            isAPrime = False
            break

    return isAPrime


circularPrimeCount =0

for y in range(2,1000000):
    iscircularPrime = isPrime(y)
    strY = str(y)
    lengthY = len(strY)
    rotationcount = 0
    while iscircularPrime and rotationcount < lengthY:
        rotationcount +=1
        iscircularPrime = iscircularPrime and isPrime(int(strY))
        firstDigit = strY[0]
        strY = strY[1:] + firstDigit
        # print strY
    if iscircularPrime:
        print y
        circularPrimeCount +=1

print circularPrimeCount
