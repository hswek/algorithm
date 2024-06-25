import sys
#n=map(int,sys.stdin.readline().rstrip().split())
#arr=list(map(int,sys.stdin.readline().rstrip().split()))
#print(min(arr),max(arr))
max_=-1
l=-1
for i in range(9):
    a=int(input())
    if a>=max_:
        l=i+1
        max_=a
print(max_)
print(l)
        