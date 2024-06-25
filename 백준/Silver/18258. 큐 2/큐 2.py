from collections import deque
import sys
n=int(input())
dq=deque()
print_list=[]
for _ in range(n):
    pp=sys.stdin.readline().rstrip().split()
    p=pp[0]
    if p=="push":
        a=(pp[1])
        dq.append(a)
    if p=="pop":
        if len(dq)==0:
            print_list.append(-1)
        else:
            print_list.append(dq.popleft())
    if p=="front":
        if len(dq)==0:
            print_list.append(-1)
        else:
            print_list.append(dq[0])
    if p=="back":
        if len(dq)==0:
            print_list.append(-1)
        else:
            print_list.append(dq[-1])
    if p=="size":
        print_list.append(len(dq))
    if p=="empty":
        if(len(dq))==0:
            print_list.append(1)
        else:
            print_list.append(0)
for i in range(len(print_list)):
    print(print_list[i])

    