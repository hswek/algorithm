import sys
#from collections import deque
#import math
#import heapq
#n,m=map(int,sys.stdin.readline().rstrip().split())
l=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
ta=a//c
if a%c!=0:
    ta+=1
tb=b//d
if b%d!=0:
    #print(b,d,b%d)
    tb+=1
print(min(l-ta,l-tb))
