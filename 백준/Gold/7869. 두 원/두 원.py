import sys
from collections import deque
import math
import heapq
#n,m=map(int,sys.stdin.readline().rstrip().split())
x1,y1,r1,x2,y2,r2=map(float,sys.stdin.readline().rstrip().split())
d=math.sqrt((x1-x2)**2+(y1-y2)**2)
#print(3**2*math.pi)
if r1>r2:
    x1,y1,r1,x2,y2,r2=x2,y2,r2,x1,y1,r1
if d>=(r1+r2):
    result= 0
elif d<=r2-r1:
    result= r1**2*math.pi
else:
    t1=math.acos((r1**2+d**2-r2**2)/(2*r1*d))
    t2=math.acos((r2**2+d**2-r1**2)/(2*r2*d))
    result=(r1**2*t1)-(r1**2*math.sin(2*t1)/2)+(r2**2*t2)-(r2**2*math.sin(2*t2)/2)
print('%.3f'%result)
