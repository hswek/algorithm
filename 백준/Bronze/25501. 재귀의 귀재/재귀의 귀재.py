import sys
def recursion(s,l, r):
    global a
    a+=1
    if(l >= r):
        return 1;
    elif(s[l] != s[r]): 
        return 0;
    else:
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

n=int(input())
for i in range(n):
    a=0
    s=sys.stdin.readline().rstrip()
    print(isPalindrome(s),a)