import sys
from collections import deque
now=1
sys.setrecursionlimit(10**5)
k=int(input())
def bfs(start,visit,arr):
    global now
    d=deque()
    d.append([start,1])
    visit[i]=1
    
    while(len(d)!=0):
        top,now=d.popleft()
        if now==1:
            opposite=2
        else:
            opposite=1
        for j in arr[top]:
            if visit[j]==now:
                return False
            if visit[j]==opposite:
                continue
            visit[j]=opposite
            d.append([j,opposite])
    return True
            
                
            
    now+=2
for _ in range(k):
    v,e=map(int,sys.stdin.readline().rstrip().split())
    arr=[[] for i in range(v+1)]
    visit=[0]*(v+1)
    for i in range(e):
        i,j=map(int,sys.stdin.readline().rstrip().split())
        arr[i].append(j)
        arr[j].append(i)
    a=2
    for i in range(1,v+1):
        if visit[i]==0:
            if bfs(i,visit,arr)==False:
                a=1
                print('NO')
                break
    if a==2:
        print('YES')