goodcombo = 0
for onepence in range(0,201):
    for twopence in range(0,((200 - onepence)/2) + 1):
        for fivepence in range(0,((200 - onepence - twopence*2)/5) + 1):
            for tenpence in range(0,((200 - onepence - twopence*2 - fivepence * 5)/10) + 1):
                for twentypence in range(0,((200 - onepence - twopence*2 - fivepence*5 - tenpence*10)/20) + 1):
                    for fiftypence in range(0,((200 - onepence - twopence*2 - fivepence*5 - tenpence*10 - twentypence*20)/50) + 1):
                        for pound in range(0,3):
                            for twopound in range(0,2):
                                if onepence + twopence *2 + fivepence*5 + tenpence*10 + twentypence*20 + 50*fiftypence + pound*100 + twopound*200 == 200:
                                    goodcombo +=1

print goodcombo


# method 2 - using recursion

coins =[200,100,50,20,10,5,2,1]

def findcombos (left,current_coin):
    possibilities = 0
    if (current_coin == 7):
        return 1
    for i in range(current_coin, 8):
        if left-coins[i] == 0:
            possibilities +=1
        if left-coins[i]>0:
            possibilities += findcombos(left-coins[i],i)
    return possibilities


print findcombos(200,0)
