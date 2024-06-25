n=int(input())
arr=[0]*n
zero=[0]*n
one=[0]*n
if n==1 or n==2:
    print(1)
else:
    one[0]=1
    one[1]=0
    zero[0]=0
    zero[1]=1
    for i in range(2,n):
        zero[i]=one[i-1]+zero[i-1]
        one[i]=zero[i-1]
    print(zero[i]+one[i])
