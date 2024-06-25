import sys
n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[i for i in range(1,n+1)]
#print( arr)
for _ in range(m):
    start,end=map(int,sys.stdin.readline().rstrip().split())
    start-=1
    end-=1
    arr[start],arr[end]=arr[end],arr[start]
    #print(arr)
for i in range(n):

    print(arr[i],end=' ')