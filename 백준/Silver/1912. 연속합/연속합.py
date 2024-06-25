import sys
from itertools import combinations
n=int(input())
arr=list(map(int,input().split()))
result=0
max_num=0
is_postivie=False
for i in range(n):
    result+=arr[i]
    if arr[i]>0:
        is_postivie=True
    max_num=max([result,max_num])
    if result<0:
        result=0
if is_postivie==False:
    max_num=max(arr)
print(max_num)