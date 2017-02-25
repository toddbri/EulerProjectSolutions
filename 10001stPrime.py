import math
primes =[]
i=2
while (len(primes)<10001):
    y=2
    i_is_prime= True
    while (y<(int(math.sqrt(i))+1)):
        if (i%y)==0:
            i_is_prime = False
            y = i
        y+=1
    if i_is_prime:
        primes.append(i)
    i+=1
print primes[len(primes)-1]
