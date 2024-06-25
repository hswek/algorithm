import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**5)
def dfs(start,visit,parent):
    if visit[start]==1:
        return False
    visit[start]=1
    is_tree=True
    for i in range(1,n+1):
        if i!=parent and arr[start][i]==1:
            if False==dfs(i,visit,start):
                is_tree=False
    return is_tree
case=1
while True:
    n,m=map(int,sys.stdin.readline().rstrip().split())
    if n==0 and m==0:
        break
    arr=[[-1]*(n+1) for i in range(n+1)]
    for i in range(m):
        start,end=map(int,sys.stdin.readline().rstrip().split())
        arr[start][end]=1
        arr[end][start]=1
    tree=0
    visit=[0]*(n+1)
    for i in range(1,n+1):
        if visit[i]==0:
            if dfs(i,visit,-1)!=False:
                tree+=1
    if tree>=2:
        print('Case '+str(case)+': A forest of '+str(tree)+' trees.')
    if tree==1:
        print('Case '+str(case)+': There is one tree.')
    if tree==0:
        print('Case '+str(case)+': No trees.')
    case+=1
    #print(tree)
