x,y=map(int,input().split())
z=int(input())
z1=z//60
z2=z%60
x+=z1
y+=z2
if y>=60:
    y-=60
    x+=1
if x>=24:
    x-=24
print(x,y)