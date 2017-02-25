product = 0
largest = 0
def isPalindrome(x):
    str_x = str(x)
    is_palindrome = True
    if (len(str_x)%2)==0:
        for a in range(len(str_x)/2):
            q = len(str_x)
            if str_x[a:a+1]!=str_x[q-a-1:q-a]:
                is_palindrome = False
    else:
        for a in range(int(len(str_x)/2)):
            q = len(str_x)
            if str_x[a:a+1]!=str_x[q-a-1:q-a]:
                is_palindrome = False
    return is_palindrome

for i in range(1000,99,-1):
    for j in range(1000,99,-1):
        if isPalindrome(i*j):
            if (i*j)>largest:
                largest = i*j
print largest
