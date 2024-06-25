import sys
n=int(input())
cache=[-1]*105
cache[0]=1
cache[1]=1
cache[2]=1
cache[3]=2
cache[4]=2
cache[5]=3
def fact(n):
    if cache[n]!=-1:
        return cache[n]
    if n<0:
        return 0
    cache[n]=fact(n-2)+fact(n-3)
    return cache[n]
for i in range(n):
    a=int(sys.stdin.readline().rstrip())
    print(fact(a-1))    