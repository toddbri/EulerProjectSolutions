choices = [0,1,2,3,4,5,6,7,8,9]
counter = 0
for a in choices:
    choicesLeft1 = choices[:]
    choicesLeft1.remove(a)
    for b in choicesLeft1:
        choicesLeft2 = choicesLeft1[:]
        choicesLeft2.remove(b)
        for c in choicesLeft2:
            choicesLeft3 = choicesLeft2[:]
            choicesLeft3.remove(c)
            for d in choicesLeft3:
                choicesLeft4 = choicesLeft3[:]
                choicesLeft4.remove(d)
                for e in choicesLeft4:
                    choicesLeft5 = choicesLeft4[:]
                    choicesLeft5.remove(e)
                    for f in choicesLeft5:
                        choicesLeft6 = choicesLeft5[:]
                        choicesLeft6.remove(f)
                        for g in choicesLeft6:
                            choicesLeft7=choicesLeft6[:]
                            choicesLeft7.remove(g)
                            for h in choicesLeft7:
                                choicesLeft8 = choicesLeft7[:]
                                choicesLeft8.remove(h)
                                for i in choicesLeft8:
                                    choicesLeft9 = choicesLeft8[:]
                                    choicesLeft9.remove(i)
                                    for j in choicesLeft9:
                                        # print choicesLeft9
                                        counter +=1
                                        # print counter
                                        # print a,b,c,d,e,f,g,h,i,j
                                        # raw_input()
                                        if counter == 1000000:
                                            print "millionth perm is :%d%d%d%d%d%d%d%d%d%d" % (a,b,c,d,e,f,g,h,i,j)
