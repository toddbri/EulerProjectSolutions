import math
spec = 1
digitCount = 0
count = 0
answer = 1
while spec < 1000001:
    count += 1
    digitCount += len(str(count))
    if digitCount >= spec:
        digit = int(count //(math.pow(10,digitCount-spec))%10)
        print 'd(%i): %i' % (spec, digit)
        answer *=digit
        spec *= 10
print 'answer is ', answer
