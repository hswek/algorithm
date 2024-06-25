import sys
from collections import deque
              
t=int(sys.stdin.readline().rstrip())
for _ in range(t):

    n,k=map(int,sys.stdin.readline().rstrip().split())

    
    arr=[-1]+list(map(int,sys.stdin.readline().rstrip().split()))
    arr2=[[] for i in range(n+1)]
    
    for i in range(k):
        i,j=map(int,sys.stdin.readline().rstrip().split())
        arr2[j].append(i)
        
    w=int(sys.stdin.readline().rstrip())
    cache=[-1]*(n+1)
    def recursive(pos):
        if cache[pos]!=-1:
            return cache[pos]
        m=0
        for i in arr2[pos]:
            m=max(m,recursive(i))
        cache[pos]=m+arr[pos]
        return cache[pos]
    print(recursive(w))