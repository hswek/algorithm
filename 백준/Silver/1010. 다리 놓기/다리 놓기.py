n=int(input())
def fact(n):
    num=1
    for i in range(1,n+1):
        num=num*i
    return num

for i in range(n):
    a,b=map(int,input().split())
    a=min(a,b-a)
    print(int(fact(b)/fact(b-a)/fact(a)))