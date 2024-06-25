import sys
a,b=map(int,sys.stdin.readline().rstrip().split())
while(a!=0 and b!=0):
    print(a+b)
    a,b=map(int,sys.stdin.readline().rstrip().split())
    