import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(n):
    arr.append(sys.stdin.readline().rstrip())
result=987654321
for x in range(n-7):
    for y in range(m-7):
        result1=0
        result2=0
        for i in range(x,x+8):
            for j in range(y,y+8):
                #print(i,j)
                if (i+j)%2==1 and arr[i][j]!='W':
                    result1+=1
                if (i+j)%2==0 and arr[i][j]!='B':
                    result1+=1
                if (i+j)%2==1 and arr[i][j]!='B':
                    result2+=1
                if (i+j)%2==0 and arr[i][j]!='W':
                    result2+=1
        #print(result1,result2)
        result=min([result,result1,result2]) 
            
print(result)

        