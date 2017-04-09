def isPalindrome(value):
    strReverse=""
    for x in range(0,int(len(value))):
        strReverse = value[x] + strReverse
    if strReverse == value:
        return True
    else:
        return False


sumOfDPs = 0
for i in range(1,1000000):
    if isPalindrome(str(i)):
        if isPalindrome(str(bin(i))[2:]):
            print i, str(bin(i))[2:]
            sumOfDPs +=i

print sumOfDPs
