import sys
#from collections import deque
#import math
#import heapq
#n,m=map(int,sys.stdin.readline().rstrip().split())
while True:
    a=sys.stdin.readline().rstrip()
    if a=='#':
        break
    result=0
    for i in a:
        if i=='a' or i=='A' or i=='o' or i=='O' or i=='e' or i=='E' or i=='u' or i=='U' or i=='i' or i=='I':
            result+=1
    print(result)