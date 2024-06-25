import sys
a,b,c=map(int,sys.stdin.readline().rstrip().split())
def mul(a,b):
    if b<=5:
        return a**b
    return mul(a,b//2)**2%c*mul(a,b%2)%c
a=a%c
print(mul(a,b))