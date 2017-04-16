def isPandigital(num):
    if str(num).count(str(0)) > 0:
        return False
    digits = [1,2,3,4,5,6,7,8,9]
    strNum = str(num)
    for i in digits:
        if strNum.count(str(i)) != 1:
            return False
    return True

largest = 0
maxTry = 9901
for i in range(1,maxTry+1):
    series = [1]
    seriesCounter = 1
    concatenatedProduct = 1
    while concatenatedProduct < 987654321:
        strProduct = ''
        for j in series:
            c = i * j
            strProduct = strProduct + str(c)
        concatenatedProduct = int(strProduct)
        if isPandigital(concatenatedProduct):
            largest = max(largest, concatenatedProduct)
            largestI = i
            largestSeries = series
            break
        seriesCounter +=1
        series.append(seriesCounter)
print "largest: %i * %r = %i " % (largestI, largestSeries, largest);
