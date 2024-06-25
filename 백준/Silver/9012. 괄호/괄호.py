from collections import deque
import sys


n=int(input())
for i in range(n):
    d=deque()
    s=sys.stdin.readline().rstrip()
    isbreak=False
    for i in range(len(s)):
        if s[i]=='(':
            d.append('(')
        elif s[i]==')':
            if len(d)!=0 and d[-1]=='(':
                d.pop()
            else:
                print('NO')
                isbreak=True
                break
    if isbreak==True:
        continue
    if len(d)!=0:
        print('NO')
        continue
    if isbreak==False:
        print('YES')
        