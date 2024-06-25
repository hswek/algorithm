import sys

def fact(n):
    if n==1:
        return 2
    return fact(n-1)*2
n=int(input())

print(fact(n))