import sys
#from collections import deque
#import math
#import heapq
#n,m=map(int,sys.stdin.readline().rstrip().split())
x=[]
y=[]
for i in range(3):
    n,m=map(int,sys.stdin.readline().rstrip().split())
    x.append(n)
    y.append(m)
if x[0]==x[1]:
    a=x[2]
elif x[1]==x[2]:
    a=x[0]
else:
    a=x[1]
if y[0]==y[1]:
    b=y[2]
elif y[1]==y[2]:
    b=y[0]
else:
    b=y[1]
print(a,b)