import sys
n=int(input())
arr=list(map(int,input().split()))
arr.insert(0,1000000)
#print(arr)
max_arr=[1]*(n+1)
for i in range(1,n+1):
    for j in range(1,i):
        if arr[j]<arr[i] and max_arr[j]>=max_arr[i]:
            max_arr[i]=max_arr[j]+1
print(max(max_arr))
