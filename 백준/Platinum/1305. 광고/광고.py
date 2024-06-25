import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
#n,m=map(int,sys.stdin.readline().rstrip().split())
#arr=list(map(int,sys.stdin.readline().rstrip().split()))
n=sys.stdin.readline().rstrip()
m=sys.stdin.readline().rstrip()
def pre_cal(m):
    begin=1
    matched=0
    arr=[0]*len(m)
    #print(arr)
    while begin+matched<len(m):
        #print(begin,matched)

        if m[begin+matched]==m[matched]:
            matched+=1
            arr[begin+matched-1]=matched
        else:
            if matched==0:
                begin+=1
            else:
                begin=begin+matched-arr[matched-1]
                matched=arr[matched-1]
    return arr

begin=0
matched=0
arr=pre_cal(m)
print(len(m)-arr[len(m)-1])
'''
print_arr=[]
#print(arr)
while begin<=len(n)-len(m):
    #print(begin,matched)

    if matched<len(m) and n[begin+matched]==m[matched]:
        matched+=1
        if matched==len(m): 
            print_arr.append(begin+1)
    else:
        if matched==0:
            begin+=1
        else:
            begin=begin+matched-arr[matched-1]
            matched=arr[matched-1]
print(len(print_arr))
for i in print_arr:
    print(i,end=' ')
'''
