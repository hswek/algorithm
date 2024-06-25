import sys
n,k=map(int,sys.stdin.readline().rstrip().split())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
arr2=[0]*(n)
arr2[0]=arr[0]
for i in range(1,n):
    arr2[i]=arr2[i-1]+arr[i]
m=0
for i in range(k-1,n):
    if i==k-1:
        m=arr2[k-1]
    else:
        m=max(m,arr2[i]-arr2[i-k])
print(m)