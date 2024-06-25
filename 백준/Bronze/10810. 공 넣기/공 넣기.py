import sys
n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[0]*(n+1)
for _ in range(m):
    start,end,k=map(int,sys.stdin.readline().rstrip().split())
    for i in range(start,end+1):
        arr[i]=k
for i in range(1,n+1):
    print(arr[i],end=' ')