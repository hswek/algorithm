import sys
from collections import deque

d=deque()
n=int(input())
print_arr=[-1]*n
arr=list(map(int,sys.stdin.readline().rstrip().split()))
arr_dict={}
for i in arr:
    if i in arr_dict:
        arr_dict[i]+=1
    else:
        arr_dict[i]=0
        
for i in range(n-1,-1,-1):
    #print(d)
    num=arr[i]
    if len(d)==0:
        print_arr[i]=-1
        d.appendleft([arr_dict[num],num])
        continue
    while(len(d)!=0):
        if d[0][0]>arr_dict[num]:
            print_arr[i]=d[0][1]
            d.appendleft([arr_dict[num],num])
            break
        else:
            d.popleft()
    if len(d)==0:
        d.appendleft([arr_dict[num],num])
            
for i in range(n):
    print(print_arr[i],end=' ')
#print()
        