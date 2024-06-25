import sys
from collections import deque
import heapq
from itertools import *
import math
sys.setrecursionlimit(10**5)
n,a=map(int,sys.stdin.readline().rstrip().split())
print_arr=[]
while True:
    if n==0:
        break
    else:
        tmp=n%a
        print_arr.append(tmp)
        n=n//a
for i in range(len(print_arr)-1,-1,-1):
    tmp=print_arr[i]
    if tmp>=10:
        print(chr(ord('A')+print_arr[i]-10),end='')
    else:
        print(print_arr[i],end='')