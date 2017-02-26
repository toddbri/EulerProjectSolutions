found = False
i=0
x=0
while not found:
    i+=1
    x+=i
    factors = []
    a=0
    while a < x:
        a+=1
        if x%a==0:
            if not a in factors:
                factors.append(a)
            if not x/a in factors:
                factors.append(x/a)
        if (factors[len(factors)-1]-a==1):
            a=x
    if len(factors)>500:
        found = True
    else:
        print x, len(factors)

print factors
print x
