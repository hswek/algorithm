import sys
#n=map(int,sys.stdin.readline().rstrip().split())
#arr=list(map(int,sys.stdin.readline().rstrip().split()))
#print(min(arr),max(arr))
n=int(input())
for i in range(n):
    s=input()
    print(s[0]+s[-1])