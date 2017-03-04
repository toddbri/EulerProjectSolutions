g = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

# g = '''75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65'''

# g ='''3 7 4 2 4 6 8 5 9 3'''

g = g.replace("\n"," ") #remove line feeds (g is a string)
g  = g.split(" ") #split string into array on spaces (g is now an array)
rows =0
for i in range(len(g)):
    g[i] = int(g[i])  #g is now an array of Ints instead of strings

print g
y = len(g)
while y>0:
    rows +=1
    y-=rows
rows -=1                        #convert rows to 0-based
print "found %d rows, starting with row 0" % rows
currentRow = rows-1
while currentRow >=0:
    print "working on row: ", currentRow
    startNode =0
    for i in range(currentRow+1):
        startNode +=i
    # print "start node: " , startNode
    endNode = startNode + currentRow
    # print "end node: ", endNode
    nextRow = currentRow + 1
    startNodeNR = 0
    for i in range(nextRow + 1):
        startNodeNR +=i    #this is the leftmost node on the next row
    for j in range(startNode,endNode+1): # for each node in the current row
        a = g[j]
        b = g[startNodeNR]
        c = g[startNodeNR + 1]
        if a+b >= a+c:
            g[j] = a+b
        else:
            g[j] = a+c
        startNodeNR+=1
    currentRow -=1
    print "-"*10

print g[0]

q=0
