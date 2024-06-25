from collections import deque
import sys


while True:
    d=deque()
    s=sys.stdin.readline().rstrip()
    if s=='.':
        break
    if s[-1]!='.':
        s+=sys.stdin.readline().rstrip()
    isbreak=False

    for i in range(len(s)):
        if s[i]=='(':
            d.append('(')
        elif s[i]==')':
            if len(d)!=0 and d[-1]=='(':
                d.pop()
            else:
                print('no')
                isbreak=True
                break
        elif s[i]=='[':
            d.append('[')
        elif s[i]==']':
            if len(d)!=0 and d[-1]=='[':
                d.pop()
            else:
                print('no')
                isbreak=True
                break
    if isbreak==True:
        continue
    if len(d)!=0:
        print('no')
        continue
    print('yes')
        