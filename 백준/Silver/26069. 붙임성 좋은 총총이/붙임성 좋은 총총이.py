import sys


n=int(input())
result=0
d=dict()
d['ChongChong']=1
for i in range(n):
    a,b=input().split()
    if a in d:
        if b in d:
            continue
        else:
            d[b]=0
            result+=1
    elif b in d:
        if a in d:
            continue
        else:
            d[a]=0
            result+=1
print(result+1)