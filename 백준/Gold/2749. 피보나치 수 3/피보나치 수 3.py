import sys
import heapq
import copy
import math
def get_ans(num):
    num=num%(15*(10**5))
    if num==0:
        return 0
    elif num==1:
        return 1
    prev=0
    now=1
    for i in range(num-1):
        next=(prev+now)%1000000
        prev,now=now,next
    return now%1000000

a=int(input())
print(get_ans(a))
    