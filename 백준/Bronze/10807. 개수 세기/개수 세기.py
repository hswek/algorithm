import sys
n=int(input())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
a=int(input())
result=0
for i in arr:
    if a==i:
        result+=1
print(result)
    