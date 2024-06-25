from collections import deque
import sys

d=deque()
n=int(input())
for i in range(n):
    arr=sys.stdin.readline().split()
    s=arr[0]
    if s=='push':
        d.appendleft(arr[1])
    elif s=='pop':
        if len(d)!=0:
            print(d.popleft())
        else:
            print(-1)
    elif s=='top':
        if len(d)!=0:
            print(d[0])
        else:
            print(-1)
    elif s=='size':
        print(len(d))
    elif s=='empty':
        if len(d)==0:
            print(1)
        else:
            print(0)
        