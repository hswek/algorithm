import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**5)
n,m,e=map(int,sys.stdin.readline().rstrip().split())
d=[[] for i in range(n+1)]
for i in range(n-1):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    d[a].append(b)
    d[b].append(a)
arr=[[] for i in range(n+1)]
q=deque()
q.append(m)
while(len(q)!=0):
    top=q.popleft()
    #print(top)
    for i in d[top]:
        if len(arr[i])==0:
            arr[top].append(i)
            q.append(i)
cache=[-1]*(n+1)
def recursive(root):
    result=1
    if cache[root]!=-1:
        return cache[root]
    for i in arr[root]:
        result+=recursive(i)
    cache[root]=result
    return result
for i in range(e):
    print(recursive(int(sys.stdin.readline().rstrip())))
    
    

