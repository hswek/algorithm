import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
arr=list(map(int,sys.stdin.readline().rstrip().split()))
result=0
def check_line(z,y,x):
    y=y/math.sqrt(2)
    
    if y>=-z/x * y +z:
        #print(1)
        return True
    else:
        return False

for l in list(permutations(arr,len(arr))):
    l=list(l)
    l.append(l[0])
    l.append(l[1])
    
    a=0
    for i in range(len(l)-2):
        #print(l,i)
        if check_line(l[i],l[i+1],l[i+2])==False:
            a=1
            break
    if a==0:
        result+=1
print(result)
