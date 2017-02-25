import math
prime_factors =[]

number = 600851475143

def isPrime(i):
    str = "\t checking if %d is a prime number:" % i
    print str,
    is_prime = True
    y = 2
    while y<int(i/2):
        if i%y==0:
            is_prime = False
            y=i
        y+=1
    print is_prime
    return is_prime

i = 1
found = False
while not found:
    i +=1
    if (number%i==0):
        other_factor = number / i
        print "Found a pair of factors(%d, %d)" % (i, other_factor)
        if isPrime(other_factor):
            print "\t %d is also a prime" % other_factor
            found = True
    if i>number:
        found = True

print "The answer is %d" % other_factor
