import sys
from collections import deque
import heapq
import math
#sys.setrecursionlimit(10**5)
n,l=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
answer=0
for i in range(n):
    now=arr[i][0]
    is_true=True
    lenth=0
    j=0
    while j<n:
        if now==arr[i][j]:
            lenth+=1
            j+=1
            continue
        if abs(arr[i][j]-now)>1:
            is_true=False
            break
        if arr[i][j]-now==1:
            if lenth>=l:
                lenth=1
                now=arr[i][j]
                j+=1
                continue
            else:
                is_true=False
                break
        elif now-arr[i][j]==1:
            if n-j<l:
               
                is_true=False
                break
            else:
                for k in range(j,j+l):
                    if arr[i][k]!=arr[i][j]:
                       
                        is_true=False
                        break
                now=arr[i][j]
                j=j+l
                lenth=0
                continue
        if j<n:
            now=arr[i][j]
        lenth+=1
        j+=1
    
    if is_true==True:
        answer+=1
        
for j in range(n):
    now=arr[0][j]
    is_true=True
    lenth=0
    i=0
    while i<n:
        if now==arr[i][j]:
            lenth+=1
            i+=1
            continue
        if abs(arr[i][j]-now)>1:
            is_true=False
            break
        if arr[i][j]-now==1:
            if lenth>=l:
                lenth=1
                now=arr[i][j]
                i+=1
                continue
            else:
                is_true=False
                break
        elif now-arr[i][j]==1:
            if n-i<l:
                is_true=False
            else:
                for k in range(i,i+l):
                    if arr[k][j]!=arr[i][j]:
                        is_true=False
                        break
                now=arr[i][j]
                i=i+l
                lenth=0
                continue
        if i<n:
            now=arr[i][j]
        lenth+=1
        i+=1
    if is_true==True:
        answer+=1
print(answer)