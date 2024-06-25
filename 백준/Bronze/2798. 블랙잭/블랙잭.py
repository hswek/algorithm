import sys
from itertools import combinations
n,m=map(int,input().split())
arr=map(int,input().split())
combi = list(combinations(arr, 3))
arr2=[]
for i in combi:
    arr2.append(sum(i))
arr2.sort()
result=0
for i in arr2:

    if i>m:
        break
    result=i
print(result)