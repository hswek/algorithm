import sys
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()
import math
print(round(sum(arr)/len(arr)))
print(arr[len(arr)//2])
tmp={}
for i in range(len(arr)):
    v=arr[i]
    if v not in tmp:
        tmp[v]=0
    else:
        tmp[v]+=1
max1=-1
max2=-1
max3=8001
arr=[]
for key,value in tmp.items():
    arr.append((value,-key))
arr.sort(reverse=True)
if len(arr)!=1 and arr[0][0]==arr[1][0]:
    print(-arr[1][1])
else:
    print(-arr[0][1])
arr=[]
for key,value in tmp.items():
    arr.append(key)
print(max(arr)-min(arr))

