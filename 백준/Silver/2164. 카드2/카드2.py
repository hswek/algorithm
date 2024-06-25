from collections import deque
import sys
n=int(input())
arr=[i for i in range(1,n+1)]
dq=deque(arr)
while(len(dq)!=1):
    dq.popleft()
    a=dq.popleft()
    dq.append(a)
a=dq.pop()
print(a)
    
    