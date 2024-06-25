import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**5)
x=[]
y=[]
for i in range(3):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    x.append(a)
    y.append(b)
vector=[]
for i in range(2):
    vector.append([x[i+1]-x[i],y[i+1]-y[i],0,x[i+1]-x[i],y[i+1]-y[i],0])
vector1=vector[0]
vector2=vector[1]
if vector1[0]*vector2[1]-vector1[1]*vector2[0]>0:
    print(1)
elif vector1[0]*vector2[1]-vector1[1]*vector2[0]<0:
    print(-1)
else:
    print(0)
    


