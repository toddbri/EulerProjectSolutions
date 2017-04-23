import math

def isPrime(x):
    for i in range(2,int(math.sqrt(x)) + 1):
        if x%i == 0:
            return False
    return True

//The following code generates all n-digit pandigital numbers for n=1-9. It starts at 987654321 and goes to 1 but stops when it finds a Prime.


depth = 9
while depth > 0:

    for a in range(depth,0,-1):
        taken =[a]
        if len(taken) == depth:
            num = ''
            for w in range(len(taken)):
                num +=str(taken[w])
            if isPrime(int(num)):
                print int(num)
                depth = 0
            break
        for b in range(depth,0,-1):
            taken = [a]
            if taken.count(b) == 0:
                taken.append(b)
                if len(taken) == depth:
                    num =''
                    for w in range(len(taken)):
                        num +=str(taken[w])
                    if isPrime(int(num)):
                        print int(num)
                        depth = 0
                    break
                for c in range(depth,0,-1):
                    taken = [a,b]
                    if taken.count(c) == 0:
                        taken.append(c)
                        if len(taken) == depth:
                            num =''
                            for w in range(len(taken)):
                                num +=str(taken[w])
                            if isPrime(int(num)):
                                print int(num)
                                depth = 0
                            break
                        for d in range(depth,0,-1):
                            taken = [a,b,c]
                            if taken.count(d) == 0:
                                taken.append(d)
                                if len(taken) == depth:
                                    num =''
                                    for w in range(len(taken)):
                                        num +=str(taken[w])
                                    if isPrime(int(num)):
                                        print int(num)
                                        depth = 0
                                    break
                                for e in range(depth,0,-1):
                                    taken = [a,b,c,d]
                                    if taken.count(e) == 0:
                                        taken.append(e)
                                        if len(taken) == depth:
                                            num =''
                                            for w in range(len(taken)):
                                                num +=str(taken[w])
                                            if isPrime(int(num)):
                                                print int(num)
                                                depth = 0
                                            break
                                        for f in range(depth,0,-1):
                                            taken = [a,b,c,d,e]
                                            if taken.count(f) == 0:
                                                taken.append(f)
                                                if len(taken) == depth:
                                                    num =''
                                                    for w in range(len(taken)):
                                                        num +=str(taken[w])
                                                    if isPrime(int(num)):
                                                        print int(num)
                                                        depth = 0
                                                    break
                                                for g in range(depth,0,-1):
                                                    taken = [a,b,c,d,e,f]
                                                    if taken.count(g) == 0:
                                                        taken.append(g)
                                                        if len(taken) == depth:
                                                            num =''
                                                            for w in range(len(taken)):
                                                                num +=str(taken[w])
                                                            if isPrime(int(num)):
                                                                print int(num)
                                                                depth = 0
                                                            break
                                                        for h in range(depth,0,-1):
                                                            taken = [a,b,c,d,e,f,g]
                                                            if taken.count(h) == 0:
                                                                taken.append(h)
                                                                if len(taken) == depth:
                                                                    num =''
                                                                    for w in range(len(taken)):
                                                                        num +=str(taken[w])
                                                                    if isPrime(int(num)):
                                                                        print int(num)
                                                                        depth = 0
                                                                    break
                                                                for i in range(depth,0,-1):
                                                                    taken = [a,b,c,d,e,f,g,h]
                                                                    if taken.count(i) == 0:
                                                                        taken = [a,b,c,d,e,f,g,h,i]
                                                                        num =''
                                                                        for w in range(len(taken)):
                                                                            num +=str(taken[w])
                                                                        if isPrime(int(num)):
                                                                            print int(num)
                                                                            depth = 0
                                                                        break
    depth -=1







def isPandigital(x):
    strx = str(x)
    if strx.count('0') > 0:
        return False
    for i in range(1,len(strx)+1):
        if strx.count(str(i)) != 1:
            return False
    return True


// The following code is the brute force method. It is very compact but takes a long time to find the answer

found = False
# while not found:
#     # print num
#     if isPrime(num):
#         if isPandigital(num):
#             print 'largest pandigital prime: ', num
#             found = True
