import sys
from collections import deque
sys.setrecursionlimit(10**5)

arr=[0]*101
visit=[0]*101

ladder,snake=map(int,sys.stdin.readline().rstrip().split())
ladder_arr=[]
for i in range(ladder):
    ladder_arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
snake_arr=[]
for i in range(snake):
    snake_arr.append(list(map(int,sys.stdin.readline().rstrip().split())))


d=deque()
d.append([1,0])
visit[1]=1

while(len(d)!=0):
    top,a=d.popleft()
    for i in range(1,7):
        tmp=top+i
        if tmp>100:
            continue
        for i,j in ladder_arr:
            if i==tmp:
                tmp=j
        for i,j in snake_arr:
            if i==tmp:
                tmp=j
        if visit[tmp]!=0:
            continue
        visit[tmp]=a+1
        d.append([tmp,a+1])
    if visit[100]!=0:
        break

print(visit[100])