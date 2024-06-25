import sys
arr=list(map(int,sys.stdin.readline().rstrip().split()))
n=[1 ,1, 2, 2 ,2 ,8]
for i in range(len(n)):
    print(n[i]-arr[i])