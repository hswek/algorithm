import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**5)
n=int(input())
x=[]
y=[]
for i in range(n):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    x.append(a)
    y.append(b)
x.append(x[0])
y.append(y[0])
x_y1=0
x1_y=0
for i in range(len(x)-1):
    x_y1+=x[i]*y[i+1]
    x1_y+=x[i+1]*y[i]
print(round(abs((x_y1-x1_y)/2),1))