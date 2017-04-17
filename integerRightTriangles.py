largestPerfectCount = 0
arrCollectionOfRightTriangles = []
largestP = 0
for p in range(3,1001):
    perfectCount = 0
    currentCollection = []
    for a in range(1,p):
        for b in range(1,p-a):
            c = p - a -b
            if a*a + b*b == c*c:
                perfectCount +=1
                currentCollection.append((a,b,c))
    if perfectCount > largestPerfectCount:
        largestPerfectCount = perfectCount
        arrCollectionOfRightTriangles = currentCollection
        largestP = p

print "largest number of solutions is for p=",largestP
print largestPerfectCount
print arrCollectionOfRightTriangles
