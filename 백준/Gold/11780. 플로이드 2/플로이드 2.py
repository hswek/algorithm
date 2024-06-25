import sys
from collections import deque
import heapq
#sys.setrecursionlimit(10**4)
v=int(sys.stdin.readline().rstrip())
e=int(sys.stdin.readline().rstrip())
arr=[[] for i in range(v+1)]
distance=[[9876543211]*(v+1) for i in range(v+1)]
parent_arr=[[-1]*(v+1) for i in range(v+1)]

for i in range(1,v+1):
    distance[i][i]=0

for i in range(e):
    i,j,w=map(int,sys.stdin.readline().rstrip().split())
    distance[i][j]=min(distance[i][j],w)


for k in range(1,v+1):
    for i in range(1,v+1):
        for j in range(1,v+1):
            if distance[i][j] > distance[i][k]+distance[k][j]:
                parent_arr[i][j]=k
                distance[i][j]=distance[i][k]+distance[k][j]    
def print_distnace(i,j,print_arr):
    
    tmp=parent_arr[i][j]
    if tmp==-1:
        return
    #print_arr.append(i)
    print_distnace(i,tmp,print_arr)
    print_arr.append(tmp)
    print_distnace(tmp,j,print_arr)  
    
for i in range(1,v+1):
    for j in range(1,v+1):
        if distance[i][j]!=9876543211:
            print(distance[i][j],end=' ')
        else:
            print(0,end=' ')
    print()
for i in range(1,v+1):
    for j in range(1,v+1):

        if i==j or distance[i][j]==9876543211:
            print(0)
            continue
        print_arr=[]
        print_arr.append(i)

        print_distnace(i,j,print_arr)
        print_arr.append(j)
        print(len(print_arr),end=' ')
        for p in print_arr:
            print(p,end=' ')
        print()