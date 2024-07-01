import sys
import heapq

min_q=[9999999999]
max_q=[99999999999]

n=sys.stdin.readline().rstrip()
for i in range(int(n)):
    next_int=int(sys.stdin.readline().rstrip())
    if next_int>max_q[0]:
        heapq.heappush(max_q,next_int)
    else:
        heapq.heappush(min_q,-next_int)
    if len(max_q)>len(min_q):
        heapq.heappush(min_q,-(heapq.heappop(max_q)))
    elif len(max_q)<len(min_q)-1:
        heapq.heappush(max_q,-(heapq.heappop(min_q)))
    print(-min_q[0])

    