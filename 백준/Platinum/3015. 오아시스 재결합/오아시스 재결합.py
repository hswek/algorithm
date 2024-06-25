import sys
from collections import deque

d=deque()
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
    
result=0
for i in range(n-1,-1,-1):
    #print(d)
    num=arr[i]
    if len(d)==0:
        d.appendleft([num,1])
        continue
    same=1
    while(len(d)!=0):
        if d[0][0]>num:
            result+=1
            d.appendleft([num,same])
            break
        elif d[0][0]==num:
            same+=d[0][1]
            result+=d[0][1]
            d.popleft()
        else:
            result+=d[0][1]
            d.popleft()
            #result+=1
            
    if len(d)==0:
        d.appendleft([num,same])
            
print(result)
#print()
        