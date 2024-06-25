import sys
import heapq

n=int(input())
arr=[]
for i in range(n):
    a=int(sys.stdin.readline().rstrip())
    if a!=0:
        if a<0:
            heapq.heappush(arr,[abs(a),-1])
        else:
            heapq.heappush(arr,[abs(a),1])
    else:
        if len(arr)==0:
            print(0)
        else:
            answer=heapq.heappop(arr)
            if answer[1]==1:
                print(answer[0])
            else:
                print(-answer[0])
    
            