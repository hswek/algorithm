import sys
n,k=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
    
arr2=[[0]*(n) for i in range(n)]
arr2[0][0]=arr[0][0]
for i in range(1,n):
    arr2[0][i]=arr[0][i]+arr2[0][i-1]
for i in range(1,n):
    arr2[i][0]=arr[i][0]+arr2[i-1][0]

    
for i in range(1,n):
    for j in range(1,n):
        
        arr2[i][j]=arr2[i-1][j]+arr2[i][j-1]-arr2[i-1][j-1]+arr[i][j]
#print(arr2)
        
        
for _ in range(k):
    i,j,i2,j2=map(int,sys.stdin.readline().rstrip().split())
    i-=1
    j-=1
    i2-=1
    j2-=1
    if i==0 and j==0:
        print(arr2[i2][j2])
    elif i==0:
        print(arr2[i2][j2]-arr2[i2][j-1])
    elif j==0:
        print(arr2[i2][j2]-arr2[i-1][j2])
    else:
        result=arr2[i2][j2]-arr2[i-1][j2]-arr2[i2][j-1]+arr2[i-1][j-1]
        print(result)