import math
total = 0
for i in range(10,999999):
    arrStr = str(i)
    sumOfFifths = 0
    for j in range(0,len(arrStr)):
        first = float(arrStr[j])
        sumOfFifths += math.pow(first,5)
    if sumOfFifths == i:
        total += sumOfFifths

print total
