import sys
#from collections import deque
#import math
#import heapq
#n,m=map(int,sys.stdin.readline().rstrip().split())
while True:
    a=sys.stdin.readline().rstrip()
    if a=='# 0 0':
        break
    a=a.split()
    print(a[0],end=' ')
    if int(a[1])>17 or int(a[2])>=80:
        print('Senior')
    else:
        print('Junior')