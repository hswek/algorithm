import sys
from collections import deque
import heapq
s=input()
s=s.upper()
arr=[0]*(111)
for i in s:
    arr[ord(i)-ord('A')]+=1
arr=[ [-arr[i],i] for i in range(111)]
#print(arr)
heapq.heapify(arr)
a,b=heapq.heappop(arr)
c,d=heapq.heappop(arr)
#print(a,b,c,d)
if a==c:
    print('?')
else:
    print(chr(ord('A')+b))