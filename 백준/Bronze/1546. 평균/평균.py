import sys
n=map(int,sys.stdin.readline().rstrip().split())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
m=max(arr)
#print(m)
tmp=[i/m*100 for i in arr]
#print(tmp)
print(sum(tmp)/len(tmp))