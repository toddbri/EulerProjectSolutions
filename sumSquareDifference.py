sumsquares =0
sum=0
for i in range(1,101):
    sumsquares +=i**2
    sum +=i
print "The answer is: ", sum**2 - sumsquares
