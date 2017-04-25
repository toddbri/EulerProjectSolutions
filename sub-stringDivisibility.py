sum = 0

depth = 9
for a in range(depth,0,-1):
    taken =[a]

    for b in range(depth,-1,-1):
        taken = [a]
        if taken.count(b) == 0:
            taken.append(b)

            for c in range(depth,-1,-1):
                taken = [a,b]
                if taken.count(c) == 0:
                    taken.append(c)

                    for d in range(depth,-1,-1):
                        taken = [a,b,c]
                        if taken.count(d) == 0:
                            taken.append(d)

                            for e in range(depth,-1,-1):
                                taken = [a,b,c,d]
                                if taken.count(e) == 0:
                                    taken.append(e)

                                    for f in range(depth,-1,-1):
                                        taken = [a,b,c,d,e]
                                        if taken.count(f) == 0:
                                            taken.append(f)

                                            for g in range(depth,-1,-1):
                                                taken = [a,b,c,d,e,f]
                                                if taken.count(g) == 0:
                                                    taken.append(g)

                                                    for h in range(depth,-1,-1):
                                                        taken = [a,b,c,d,e,f,g]
                                                        if taken.count(h) == 0:
                                                            taken.append(h)

                                                            for i in range(depth,-1,-1):
                                                                taken = [a,b,c,d,e,f,g,h]
                                                                if taken.count(i) == 0:
                                                                    taken = [a,b,c,d,e,f,g,h,i]

                                                                    for j in range(depth,-1,-1):
                                                                        taken = [a,b,c,d,e,f,g,h,i]
                                                                        if taken.count(j) == 0:
                                                                            taken = [a,b,c,d,e,f,g,h,i,j]
                                                                            num =''
                                                                            for w in range(len(taken)):
                                                                                num +=str(taken[w])
                                                                            # print num

                                                                            if ((taken[1]*100 + taken[2]* 10 + taken[3])%2 == 0):
                                                                                # print (taken[1]*100 + taken[2]* 10 + taken[3])
                                                                                if((taken[2]*100 + taken[3] *10 + taken[4]) % 3 == 0):
                                                                                    if ((taken[3]*100 + taken[4]*10 + taken[5])%5 == 0):
                                                                                        if ((taken[4]*100 + taken[5]*10 + taken[6])%7 == 0):
                                                                                            if ((taken[5]*100 + taken[6]*10 + taken[7])%11 == 0):
                                                                                                if ((taken[6]*100 + taken[7]*10 + taken[8])%13 == 0):
                                                                                                    if ((taken[7]*100 + taken[8]*10 + taken[9])%17 == 0):
                                                                                                            sum += int(num)
                                                                                                            print num

print 'sum: %i' % sum
