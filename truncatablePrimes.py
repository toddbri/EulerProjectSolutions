import math
count = 0
sum = 0
def isPrime(num):
    if num == 1:
        return False
    for i in range(2,int(math.sqrt(num)+1)):
        if num%i == 0:
            return False
    return True


x = 11
while count < 11:
    if isPrime(x):
        a = int(x/10)
        powerOfTen = 10
        rightToLeftIsPrime = True
        while a >= 1 and rightToLeftIsPrime==True:
            if isPrime(a):
                a = int(a/10)
                powerOfTen *=10
            else:
                rightToLeftIsPrime = False
        if rightToLeftIsPrime:
            a = x - int(x/powerOfTen)*powerOfTen
            powerOfTen /=10
            leftToRightIsPrime = True
            while a>=1 and leftToRightIsPrime == True:
                if isPrime(a):
                    a = a - int(a/powerOfTen)*powerOfTen
                    powerOfTen /=10
                else:
                    leftToRightIsPrime = False

        if rightToLeftIsPrime == True and leftToRightIsPrime == True:
            print x
            count += 1
            sum +=x
    x +=1

print "sum is: ", sum
