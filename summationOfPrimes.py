import math
sum = 0
highestprime = 2000000
def isPrime(i):
    is_prime = True
    y = 2
    while y<=int(math.sqrt(i)):
        if i%y==0:
            is_prime = False
            y=i
        y+=1
    return is_prime
x = 1
while x<highestprime:
    x+=1
    if isPrime(x):
        sum +=x
        print "%d is prime. Sum is: %d" %(x,sum)
print ""
print "The answer is: ", sum
print "" 
