import sys
d={}
for i in range(10):
    a=int(input())%42
    if a in d:
        continue
    else:
        d[a]=1
print(len(d))