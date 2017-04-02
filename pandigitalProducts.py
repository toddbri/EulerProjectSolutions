arrProducts = []
sumProducts = 0
arrDigits = [1,2,3,4,5,6,7,8,9]
for i in range(1,101):
    for j in range(1,2001):
        product = i*j
        a = str(i)
        b = str(j)
        c = str(product)
        identity = a+b+c
        if len(identity) == 9:
            pandigital = True
            for k in range(1,10):
                if str(k) not in identity:
                    pandigital = False
                    break
            if pandigital:
                if product not in arrProducts:
                    print a,b,c
                    arrProducts.append(product)
                    sumProducts +=product

print 'the sum of the unique products: ', sumProducts
