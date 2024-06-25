from collections import deque
import sys
import copy
n,k=list(map(int,input().split()))
arr=[i for i in range(n)]
a=list(map(int,input().split()))
b=[i-1 for i in a]
dq=deque(arr)
now=0
result=0
while(len(b)!=0):
    if dq[0]==b[0]:
        dq.popleft()
        b.pop(0)
    else:
        #print(dq[0],b[0])
        left=0
        left_dq=copy.deepcopy(dq)
        while(left_dq[0]!=b[0]):
            tmp=left_dq.popleft()
            left_dq.append(tmp)
            left+=1
        right_dq=copy.deepcopy(dq)
        right=0
        while(right_dq[0]!=b[0]):
            tmp=right_dq.pop()
            right_dq.appendleft(tmp)
            right+=1
        if left<right:
            #print("left:",left)
            result+=left
            dq=copy.deepcopy(left_dq)
        else:
            result+=right
            #print("right:",right)
            dq=copy.deepcopy(right_dq)
print(result)