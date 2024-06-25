from collections import deque
import sys
nu=int(input())
for _ in range(nu):
    n,k=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    num_arr=[0]*(10)
    ori_arr=[i for i in range(n)]
    for i in range(n):
        num_arr[arr[i]]+=1
    dq=deque(arr)
    ori_arr=deque(ori_arr)
    when=0
    while(len(dq)!=0):
    
        a=dq.popleft()
        b=ori_arr.popleft()
        is_end=0
        for i in range(1,10):
            if i>a and num_arr[i]!=0:
                is_end=1
                dq.append(a)
                ori_arr.append(b)
                break;
        if is_end==1:
            continue
        num_arr[a]-=1
        when+=1
        if b==k:
            print(when)
            break
   