import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**5)
v,e=map(int,sys.stdin.readline().rstrip().split())
arr=[[9876543210]*(v+1) for i in range(v+1)]
for i in range(e):
    a,b,c=map(int,sys.stdin.readline().rstrip().split())
    arr[a][b]=c
for i in range(v+1):
    arr[i][i]=0
for k in range(1,v+1):
    for i in range(1,v+1):
        for j in range(1,v+1):
            arr[i][j]=min(arr[i][j],arr[i][k]+arr[k][j])
result=9876543210
for i in range(1,v+1):
    for j in range(1,v+1):
        if i==j:
            continue
        if arr[i][j]==9876543210 or arr[j][i]==9876543210:
            continue
        else:
            result=min(result,arr[i][j]+arr[j][i])
if result==9876543210:
    print(-1)
else:
    print(result)