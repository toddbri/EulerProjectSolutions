num_to_words={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",
    11:"eleven", 12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen", 18:"eighteen",
    19:"nineteen", 20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",100:"onehundred",
    200:"twohundred",300:"threehundred",400:"fourhundred",500:"fivehundred",600:"sixhundred",700:"sevenhundred",
    800:"eighthundred",900:"ninehundred"}

limit = 1000
sum = 0

for x in range(1,limit+1):
    i=x
    words =""
    hundreds = 0
    if i==1000:
        sum +=11 #11 letters in one thousand
        i =0
        words = "one thousand"
    if i>=100:
        hundreds = i-i%100
        sum+=len(num_to_words[hundreds])
        i-=hundreds
        words = num_to_words[hundreds]
    if i>19:
        if hundreds >0:
            words +=" and "
            sum +=3
        tens = i - i%10
        sum +=len(num_to_words[tens])
        words +=num_to_words[tens]
        i -=tens
        if i >0:
            sum+=len(num_to_words[i])
            if hundreds >0 and tens<20:
                words += " and "
                sum +=3
            words += num_to_words[i]
            i=0
    if i>0:
        if hundreds >0:
            words += " and "
            sum+=3
        sum +=len(num_to_words[i])
        words +=num_to_words[i]
    print x, words
print sum
