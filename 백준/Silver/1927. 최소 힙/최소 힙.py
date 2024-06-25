import sys
import heapq

n=int(input())
arr=[]
for i in range(n):
    a=int(sys.stdin.readline().rstrip())
    if a!=0:
        heapq.heappush(arr,a)
    else:
        if len(arr)==0:
            print(0)
        else:
            answer=heapq.heappop(arr)
            print(answer)
    