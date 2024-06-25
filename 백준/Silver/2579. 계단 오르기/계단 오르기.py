import sys
n=int(input())
arr=[0]*(n+1)
for i in range(1,n+1):
    arr[i]=int(input())
max_zero=[0]*(n+1)
max_one=[0]*(n+1)
max_two=[0]*(n+1)
#max_one[1]=arr[1]
if n==1:
    print(arr[1])
else:
    max_one[1]=arr[1]
    max_zero[1]=arr[1]
    for i in range(2,n+1):
        max_zero[i]=max([ max_zero[i-2],max_one[i-2]])+arr[i]
        max_one[i]=max_zero[i-1]+arr[i]
        #max_two[i]=max_one[i-1]+arr[i]
    print(max([max_one[n],max_zero[n]]))