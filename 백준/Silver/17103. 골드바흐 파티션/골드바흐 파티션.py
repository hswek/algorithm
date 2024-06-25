import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
#n,m=map(int,sys.stdin.readline().rstrip().split())
#arr=list(map(int,sys.stdin.readline().rstrip().split()))
def is_prime(a):
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            return 0
    return 1
n=int(input())
prime=[1]*1000001
for i in range(2,int(math.sqrt(1000001))+1):
    if prime[i]==1:
        for j in range(2*i,1000001,i):
            prime[j]=0
        
#arr=list(map(int,sys.stdin.readline().rstrip().split()))
for _ in range(n):
    a=int(input())
    
    result=0
    arr=[]
    for i in range(2,a//2+1):
        if prime[i]==1 and prime[a-i]==1:
            result+=1
    print(result)        
    