import sys
from collections import deque
sys.setrecursionlimit(10**5)
subin,sister=map(int,sys.stdin.readline().rstrip().split())
visit=[0]*100010

d=deque()
d.append([subin,0])
while(len(d)!=0):
    now,a=d.popleft()
    if now== sister:
        print(a)
        break
    pos=[1,-1,now]
    for i in pos:
        nx=now+i
        if nx>=100001 or nx<0 or visit[nx]==1:
            continue
        visit[nx]=1
        d.append([nx,a+1])
    