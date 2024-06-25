import sys
n=int(input())
result=9
if n==1:
    print(9)
elif n==2:
    print(17)
else:
    x0=[0]*(n+1)
    x1=[0]*(n+1)
    x2=[0]*(n+1)
    x3=[0]*(n+1)
    x4=[0]*(n+1)
    x5=[0]*(n+1)
    x6=[0]*(n+1)
    x7=[0]*(n+1)
    x8=[0]*(n+1)
    x9=[0]*(n+1)
    x0[1]=1
    x1[1]=1
    x2[1]=1
    x3[1]=1
    x4[1]=1
    x5[1]=1
    x6[1]=1
    x7[1]=1
    x8[1]=1
    x9[1]=1
    for i in range(2,n+1):
        x0[i]=x1[i-1]
        x1[i]=x0[i-1]+x2[i-1]
        x2[i]=x1[i-1]+x3[i-1]
        x3[i]=x2[i-1]+x4[i-1]
        x4[i]=x3[i-1]+x5[i-1]
        x5[i]=x4[i-1]+x6[i-1]
        x6[i]=x5[i-1]+x7[i-1]
        x7[i]=x6[i-1]+x8[i-1]
        x8[i]=x7[i-1]+x9[i-1]
        x9[i]=x8[i-1]
    print((x1[n]+x2[n]+x3[n]+x4[n]+x5[n]+x6[n]+x7[n]+x8[n]+x9[n])%1000000000)
