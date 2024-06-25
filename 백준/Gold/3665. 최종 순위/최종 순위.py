import sys
from collections import deque
import math
sys.setrecursionlimit(10**4)
#t=int(sys.stdin.readline().rstrip())
#n,k=map(int,sys.stdin.readline().rstrip().split())
#arr=[-1]+list(map(int,sys.stdin.readline().rstrip().split()))
t=int(sys.stdin.readline().rstrip())
for _ in range(t):
    n=int(sys.stdin.readline().rstrip())
    rank2team=[-1]+list(map(int,sys.stdin.readline().rstrip().split()))
    n2=int(sys.stdin.readline().rstrip())
    is_root=[0]*(n+1)
    arr2=[[0] * (n+1) for i in range(n+1)]
    team2rank=[0]*(n+1)
    for i in range(1,n+1):
        tmp=rank2team[i]
        team2rank[tmp]=i

    for i in range(1,n+1):
        for j in range(1,n+1):
            if team2rank[i]<team2rank[j]:
                arr2[i][j]=1
                is_root[j]+=1
    
    for __ in range(n2):
        i,j=map(int,sys.stdin.readline().rstrip().split())
        if arr2[i][j]==1:
            arr2[j][i]=1
            arr2[i][j]=0
            is_root[j]-=1
            is_root[i]+=1
        else:
            arr2[j][i]=0
            arr2[i][j]=1
            is_root[i]-=1
            is_root[j]+=1
    root=-1
    for i in range(1,n+1):
        a=True
        for j in range(1,n+1):
            if i==j:
                continue
            if arr2[i][j]==0:
                a=False
                break
        if a==True:
            root=i
    #print(arr2,root)
    if root==-1:
        print('IMPOSSIBLE')
        continue
    q=deque()
    q.append(root)
    visit=[0]*(n+1)
    is_visit=[False]*(n+1)
    def dfs(root):
        for i in range(1,n+1):
            if arr2[root][i]==0 :
                continue
            if visit[i]==True:
                return False
            if is_visit[i]==True:
                continue
            visit[i]=True
            if dfs(i)==False:
                return False
            visit[i]=False
            is_visit[i]=True
        return True
    
    if dfs(root)==False:
        print('IMPOSSIBLE')
        continue
        
    is_good=True
    print_arr=[]
    while len(q)!=0:
        
        top=q.popleft()
        print_arr.append(top)
        a=0
        for i in range(1,n+1):
            if arr2[top][i]==0:
                continue
            is_root[i]-=1
            if is_root[i]==0:
                q.append(i)
                
                a+=1
        if a>1:
            print('?')
            is_good=False
            break
    if is_good==False:
        continue
    if len(print_arr)!=n:
        print('?')
    aaa=[0]*(n+1)
    for i in range(n):
        print(print_arr[i],end=' ')

    print()
        
        
        
        
        
        
        
    