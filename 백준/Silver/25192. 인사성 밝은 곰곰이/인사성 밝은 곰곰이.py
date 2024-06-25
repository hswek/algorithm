import sys


n=int(input())
d=dict()
result=0
for i in range(n):
    s=input()
    if s=='ENTER':
        d=dict()
        continue
    if s not in d:

        result+=1
        d[s]=0
print(result)