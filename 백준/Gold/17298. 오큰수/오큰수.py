import sys
from collections import deque

d=deque()
n=int(input())
print_arr=[-1]*n
arr=list(map(int,sys.stdin.readline().rstrip().split()))
for i in range(n-1,-1,-1):
    #print(d)
    num=arr[i]
    if len(d)==0:
        print_arr[i]=-1
        d.appendleft(num)
        continue
    while(len(d)!=0):
        if d[0]>num:
            print_arr[i]=d[0]
            d.appendleft(num)
            break
        else:
            d.popleft()
    if len(d)==0:
        d.appendleft(num)
            
for i in range(n):
    print(print_arr[i],end=' ')
#print()
        