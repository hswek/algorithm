import sys
n=int(input())
result=9
if n==1:
    print(10)
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
    x_list=[x0,x1,x2,x3,x4,x5,x6,x7,x8,x9]
    for i in range(2,n+1):
        for j in range(len(x_list)):
            for z in range(j,len(x_list)):
                x_list[j][i]+=x_list[z][i-1]
    print((x0[n]+x1[n]+x2[n]+x3[n]+x4[n]+x5[n]+x6[n]+x7[n]+x8[n]+x9[n])%10007)

