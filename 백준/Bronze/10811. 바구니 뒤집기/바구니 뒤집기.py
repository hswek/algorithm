import sys
n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[i for i in range(1,n+1)]

for _ in range(m):
    start,end=map(int,sys.stdin.readline().rstrip().split())
    start-=1
    end-=1
    tmp=arr[start:end+1]
    for i in range(end-start+1):
        arr[start+i]=tmp[-1-i]
for i in range(n):
    print(arr[i],end=' ')