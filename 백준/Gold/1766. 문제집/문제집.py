import sys
from collections import deque
import heapq
import math
sys.setrecursionlimit(10**4)
#t=int(sys.stdin.readline().rstrip())
#n,k=map(int,sys.stdin.readline().rstrip().split())
#arr=[-1]+list(map(int,sys.stdin.readline().rstrip().split()))
n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[[] for i in range(n+1)]
directed=[0]*(n+1)

for z in range(m):
    i,j=map(int,sys.stdin.readline().rstrip().split())
    arr[i].append(j)
    directed[j]+=1
root=-1

for i in range(1,n+1):

    if directed[i]==0:
        root=i
        break
q=[root]
heapq.heapify(q)

#q.append(root)
visit=[0]*(n+1)
visit[root]=True
#print(directed)
while len(q):
    top=heapq.heappop(q)
    #print(directed)
    print(top,end=' ')
    for i in arr[top]:
            directed[i]-=1
    for i in range(1,n+1):
        if directed[i]==0 and visit[i]==False:
            heapq.heappush(q,i)
            visit[i]=True
                
    
        
    