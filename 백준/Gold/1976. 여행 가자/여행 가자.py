import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**5)
#n,m=map(int,sys.stdin.readline().rstrip().split())
n=int(input())
m=int(input())

arr=[[]]
for i in range(n):
    arr.append([-1]+list(map(int,sys.stdin.readline().rstrip().split())))
visit_arr=list(map(int,sys.stdin.readline().rstrip().split()))
def find(element):
    if parent_arr[element]==-1:
        return element
    parent_arr[element]=find(parent_arr[element])
    return parent_arr[element]
def union(a,b):
    a_mom=find(a)
    b_mom=find(b)
    if b_mom==a_mom:
        return
    parent_arr[b_mom]=a_mom
    return
parent_arr=[-1]*(n+1)
for i in range(1,n+1):
    for j in range(1,n+1):
        if arr[i][j]==1:
            union(i,j)
a=0
for i in visit_arr:
    if find(i)!=find(visit_arr[0]):
        print('NO')
        a=1
        break
#print(parent_arr)
if a==0:
    print('YES')

    