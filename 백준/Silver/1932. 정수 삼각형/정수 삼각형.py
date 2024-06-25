import sys
n=int(input())
arr=[0]
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(2,n+1):
    for j in range(i):
        if j==0:
            arr[i][j]+=arr[i-1][j]
        elif j==i-1:
            arr[i][j]+=arr[i-1][j-1]
        else:
            x1=arr[i-1][j]
            x2=arr[i-1][j-1]
            if x1>x2:
                arr[i][j]+=x1
            else:
                arr[i][j]+=x2
if n==1:
    print(arr[1][0])
else:
    print(max(arr[i]))
