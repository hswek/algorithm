import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**6)
n=int(sys.stdin.readline().rstrip())

d=[[] for i in range(n+1)]
for i in range(n-1):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    d[a].append(b)
    d[b].append(a)
arr=[[] for i in range(n+1)]
q=deque()
q.append(1)
while(len(q)!=0):
    top=q.popleft()
    #print(top)
    for i in d[top]:
        if len(arr[i])==0:
            arr[top].append(i)
            q.append(i)


def make_adapter(root):
    #if cache[root]!=-1:
    #    return cache[root]
    result=0
    r=False
    for i in arr[root]:
        tmp,is_true=make_adapter(i)
        result+=tmp
        if is_true==False:
            r=True
    if r==True:
        result+=1
    #cache[root]=[result,r]
    return result,r
        
print(make_adapter(1)[0])
    
    

