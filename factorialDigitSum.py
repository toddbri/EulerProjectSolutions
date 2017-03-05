def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

x = factorial(100)
strx = str(x)
sum =0
for digit in strx:
    sum+=int(digit)

print sum
