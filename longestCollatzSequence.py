cap = 1000000
largest = 0
def collatz(x, count):
    count +=1
    if x == 1:
        return count
    else:
        if x%2==0:
            return collatz(x/2,count)
        else:
            return collatz(3*x + 1,count)
i = 1
while i < cap:
    i+=1
    s = collatz(i,0)
    if s > largest:
        largest = s
        print i, largest
