import math
arrDistincts=[];
upperLimit = 100;
for a in range(2,upperLimit+1):
  for b in range(2,upperLimit+1):
    element = math.pow(a,b)
    found = False
    for i in range(0,len(arrDistincts)):
        if arrDistincts[i] == element:
            found = True
    if not found:
        arrDistincts.append(element)


print "number of distinct terms: " , len(arrDistincts)
