n =[]
n.append(0)
n.append(1)
i = 2
sum =0
too_large = False
while not too_large:
    n.append(n[i-1] + n[i-2])

    if n[i] > 4000000:
        too_large=True
    else:
        if n[i]%2==0:
            sum +=n[i]
    i +=1

print sum
