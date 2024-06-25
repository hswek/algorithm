n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    num=1
    a=a%10
    for j in range(b):
        num=num*a
        num=num%10
    if num==0:
        num=10
    print(num)