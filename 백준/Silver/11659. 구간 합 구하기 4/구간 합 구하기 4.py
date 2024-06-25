import sys
n,k=map(int,sys.stdin.readline().rstrip().split())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
arr2=[0]*(n)
arr2[0]=arr[0]
for i in range(1,n):
    arr2[i]=arr2[i-1]+arr[i]
for i in range(k):
    i,j=map(int,sys.stdin.readline().rstrip().split())
    i-=1
    j-=1
    if i==0:
        print(arr2[j])
    else:
        print(arr2[j]-arr2[i-1])
        