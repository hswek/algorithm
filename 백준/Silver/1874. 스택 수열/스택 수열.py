from collections import deque
import sys

n=int(sys.stdin.readline().rstrip())
arr=[True]*100001
p=[]
d=deque()
now=0
isbreak=False
for i in range(n):
    s=int(sys.stdin.readline().rstrip())
    if s>now:
        for i in range(now+1,s+1):
            d.append(i)
            p.append('+')
        d.pop()
        p.append('-')
        now=s
    else:
        if s!=d[-1]:
            print('NO')
            isbreak=True
            break
        else:
            d.pop()
            p.append('-')
if isbreak==False:
    for i in range(len(p)):
        print(p[i])