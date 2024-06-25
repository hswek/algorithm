import sys


n=int(input())
arr=list(map(int,input().split()))
min2=987654321
max2=0
for i in range(n):
    max2=max(max2,arr[i])
    min2=min(min2,arr[i])
print(max2*min2)