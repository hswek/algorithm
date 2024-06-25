import sys
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
arr.sort(key=lambda x:(x[1],x[0]))
result=0
now=0
for i in arr:
    if i[0]<now:
        continue
    else:
        now=i[1]
    result+=1
print(result)