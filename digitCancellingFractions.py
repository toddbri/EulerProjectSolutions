dout = 1
for i in range(11,100):
    for j in range(10,i):
        n = float(j)
        d = float(i)
        original = n/d
        stri = str(i)
        strj = str(j)
        if stri[0] == strj[0] and stri[0]!= '0' and stri[1] !='0':
            new_n = float(strj[1])
            new_d = float(stri[1])
            if new_n/new_d == original:
                print j, i, new_n, new_d
                dout *= new_d
        if stri[0] == strj[1] and stri[0]!= '0' and stri[1] != '0':
            new_n = float(strj[0])
            new_d = float(stri[1])
            if new_n/new_d == original:
                print j, i, new_n, new_d
                dout *= new_d
        if stri[1] == strj[1] and stri[1]!= '0' and stri[0] != '0':
            new_n = float(strj[0])
            new_d = float(stri[0])
            if new_n/new_d == original:
                print j, i, new_n, new_d
                dout *= new_d
        if stri[1] == strj[0] and stri[1]!= '0' and stri[0] != '0':
            new_n = float(strj[1])
            new_d = float(stri[0])
            if new_n/new_d == original:
                print j, i, new_n, new_d
                dout *= new_d
print dout
