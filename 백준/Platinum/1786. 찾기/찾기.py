import sys
from collections import deque
import heapq
import math
sys.setrecursionlimit(10**5)
#t=int(sys.stdin.readline().rstrip())
#n,k=map(int,sys.stdin.readline().rstrip().split())
#arr=[-1]+list(map(int,sys.stdin.readline().rstrip().split()))
#n,m=map(int,sys.stdin.readline().rstrip().split())

t=input()
p=input()

begin=1
matched=0
arr=[0]*len(p)
while begin+matched<len(p):
    if p[begin+matched]==p[matched]:
        matched+=1
        arr[begin+matched-1]=matched
    else:
        if matched==0:
            begin+=1
        else:
            begin=begin+matched-arr[matched-1]
            matched=arr[matched-1]
begin=0
matched=0
print_arr=[]
while begin<=len(t)-len(p):
    #print(begin,matched)
    if matched<len(p)and t[begin+matched]==p[matched]:
        matched+=1
        if matched==len(p):
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