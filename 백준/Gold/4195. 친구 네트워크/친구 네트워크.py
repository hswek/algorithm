import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**5)
#n,m=map(int,sys.stdin.readline().rstrip().split())
def find(element):
    if parent_arr[element][0]==-1:
        return element,parent_arr[element][1]
    parent_arr[element]=find(parent_arr[element][0])
    return parent_arr[element]
def union(a,b):
    a_mom,a_num=find(a)
    b_mom,b_num=find(b)
    if b_mom==a_mom:
        return max(a_num,b_num)
    parent_arr[b_mom]=[a_mom,-1]
    parent_arr[a_mom]=[-1,a_num+b_num]
    return a_num+b_num
T=int(input())
parent_arr={}

for _ in range(T):
    n=int(input())
    
    parent_arr={}
    for i in range(n):
        
        a,b=sys.stdin.readline().rstrip().split()
        if a not in parent_arr:
            parent_arr[a]=[-1,1]
        if b not in parent_arr:
            parent_arr[b]=[-1,1]
        
        print(union(a,b))
        #print(parent_arr)


