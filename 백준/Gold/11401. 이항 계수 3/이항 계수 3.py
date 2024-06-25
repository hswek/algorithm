import sys
n,k=map(int,sys.stdin.readline().rstrip().split())
def fact(n):
    result=1
    for i in range(1,n+1):
        result=result*i%1000000007
    return result
result=1
def mul(a,b):
    if b<=5:
        return a**b
    return mul(a,b//2)**2*mul(a,b%2)%1000000007
result=fact(n)* mul(fact(n-k)*fact(k),1000000005)%1000000007
print(int(result))