from collections import deque
import sys

d=deque()
n=int(input())
for i in range(n):
    num=int(sys.stdin.readline().rstrip())
    if num==0:
        d.popleft()
    else:
        d.appendleft(num)
print(sum(d))
        