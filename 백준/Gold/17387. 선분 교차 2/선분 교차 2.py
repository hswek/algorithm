import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
x1,y1,x2,y2=list(map(int,sys.stdin.readline().rstrip().split()))
x3,y3,x4,y4=list(map(int,sys.stdin.readline().rstrip().split()))

def check_line(x1,y1,x2,y2,x3,y3):
    
    vec1=[x2-x1,y2-y1]
    vec2=[x3-x2,y3-y2]
    
    if vec1[0]*vec2[1]-vec1[1]*vec2[0]>0:
        return 1
    elif vec1[0]*vec2[1]-vec1[1]*vec2[0]==0:
        return 0
    else:
        return -1
#print(check_line(x1,y1,x2,y2,x3,y3)*check_line(x1,y1,x2,y2,x4,y4),check_line(x3,y3,x4,y4,x1,y1)*check_line(x3,y3,x4,y4,x2,y2))
if check_line(x1,y1,x2,y2,x3,y3)*check_line(x1,y1,x2,y2,x4,y4)==0 and check_line(x3,y3,x4,y4,x1,y1)*check_line(x3,y3,x4,y4,x2,y2)==0:
    
    if x2<x1:
        x1,x2=x2,x1
    if x4<x3:
        x3,x4=x4,x3
    if y2<y1:
        y1,y2=y2,y1
    if y4<y3:
        y3,y4=y4,y3
    
    if x2>=x3 and x1<=x4 and y2>=y3 and y1<=y4 :
        print(1)
    else:
        print(0)
elif check_line(x1,y1,x2,y2,x3,y3)*check_line(x1,y1,x2,y2,x4,y4)<=0 and check_line(x3,y3,x4,y4,x1,y1)*check_line(x3,y3,x4,y4,x2,y2)<=0:
    print(1)

        
else:
    print(0)

