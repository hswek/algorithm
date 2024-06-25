import sys

def fact(n):
    if n==1:
        return 1
    return fact(n-1)*n
n=int(input())
if n==0:
    print(1)
else:    
    print(fact(n))