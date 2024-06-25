x=int(input())
_=int(input())
for i in range(_):
    a,b=map(int,input().split())
    x-=a*b
if x==0:
    print("Yes")
else:
    print("No")