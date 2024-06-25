import sys
from collections import deque
s=input()
a=0
for i in range(len(s)//2):
    if s[i]!=s[-i-1]:
        print(0)
        a=1
        break
if a==0:
    print(1)