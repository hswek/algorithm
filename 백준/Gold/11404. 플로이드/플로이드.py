import sys
from collections import deque
import heapq
now=1
sys.setrecursionlimit(10**5)
v=int(sys.stdin.readline().rstrip())
e=int(sys.stdin.readline().rstrip())



q=[]
distance=[[987654321]*(v+1) for i in range(v+1)]
for i in range(e):
    i,j,w=map(int,sys.stdin.readline().rstrip().split())
    distance[i][j]=min(w,distance[i][j])
for i in range(1,v+1):
    distance[i][i]=0

for k in range(1,v+1):
    for i in range(1,v+1):
        for j in range(1,v+1):
            distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])   
            
for i in range(1,v+1):
    for j in range(1,v+1):
        if distance[i][j]==987654321:
            print('0',end=' ')
        else:
            print(distance[i][j],end=' ')
    print()