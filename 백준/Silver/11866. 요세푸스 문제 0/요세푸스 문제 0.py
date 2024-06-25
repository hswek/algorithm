from collections import deque
import sys
n,k=map(int,input().split())
arr=[i for i in range(1,n+1)]
dq=deque(arr)
print_list=[]
while(len(dq)!=0):
    for _ in range(k-1):
        dq.append(dq.popleft())
    a=dq.popleft()
    print_list.append(a)
a="<"
for i in print_list:
    a+=str(i)
    a+=', '
a=a[:len(a)-2]
print(a+'>')