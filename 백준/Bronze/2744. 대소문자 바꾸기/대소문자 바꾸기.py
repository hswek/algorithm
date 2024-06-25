import sys
from collections import deque
import heapq
#a,b,c,d,e=map(int,sys.stdin.readline().rstrip().split())
n=input()
for i in n:
    if i.islower():
        print(i.upper(),end='')
    else:
        print(i.lower(),end='')