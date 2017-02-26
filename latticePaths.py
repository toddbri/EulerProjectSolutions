r = 20  # r is the dimension of the grid horizontally (ie: the number of right moves)
d = 20 # d is the dimension of the grid vertically (ie: the number of down moves)

# This is the same as having a box with r-rights and d-downs in it. All moves must be used to get from corner to corner.
# The number of permutations is (r + d) factorial or (r+d)! if each right and down was unique. (they are not)
# Since all the rights and downs are the same, the order that the rights are picks doesn't matter.
# and the same with the order of the downs.
# therefor we must divide the number of permuations by the number of permuations of both the rights (r!) and downs (d!)
# so the answer is (r+d)!/(r!*d!)
x=1
y=1
z=1
for a in range(r+d,0,-1):
    x*=a                # x is (r+d)!
for b in range(r,0,-1):
    y*=b                # y is r!
for c in range(d,0,-1):
    z*=c                # z is d!

print "The answer is: %d" % (x/(y*z))
