n=int(input())
arr=[0]*(40+1)
arr[1]=1
arr[2]=2
arr[3]=2
arr[4]=3
arr[5]=5
for i in range(5,41):
    arr[i]=arr[i-1]+arr[i-2]

print(arr[n])
print(n-2)
