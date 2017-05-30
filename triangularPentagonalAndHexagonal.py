def triangle(n):
    return (n*(n+1))/2

def pentagonal(n):
    return (n*(3*n-1))/2

def hexagonal(n):
    return n*(2*n - 1)

arrPentagonal = []
arrHexagonal = []
found = False
t = 285
p = 165
h = 143

T = triangle(t)
P = pentagonal(p)
H = hexagonal(h)

# for x in range(1,h):
#     H = hexagonal(x)
#     arrHexagonal.append(H)
#
# for x in range(1,p):
#     P = pentagonal(x)
#     arrPentagonal.append(P)
# print T,P,H
# print len(arrHexagonal)
# print len(arrPentagonal)
while not found:
    t += 1
    T = triangle(t)

    while P < T:
        p += 1
        P = pentagonal(p)
        arrPentagonal.append(P)

    while H < T:
        h += 1
        H = hexagonal(h)
        arrHexagonal.append(H)

    if arrPentagonal.count(T) > 0 and arrHexagonal.count(T) > 0:
        found = True
        h1 = arrHexagonal[arrHexagonal.index(T)]
        p1 = arrPentagonal[arrPentagonal.index(T)]
        print t, T, h1, p1





q = 1
