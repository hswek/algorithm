import sys
from collections import deque
import math
import heapq
#n,m=map(int,sys.stdin.readline().rstrip().split())

    
x,y,d,t=map(int,sys.stdin.readline().rstrip().split())
l=math.sqrt(x**2+y**2)
if l>=d:
    j=l//d
    result=min([l,j*t+l-j*d,t+j*t])
else:
    result=min([l,t*2,t+d-l])
print(result)