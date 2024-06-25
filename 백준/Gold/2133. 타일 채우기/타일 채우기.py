n=int(input())
arr=[0]*(31)
arr[2]=3
for i in range(4,31):
    if i%2==0:
        arr[i]+=3*arr[i-2]
        for j in range(4,i):
            arr[i]+=2*arr[i-j]
        arr[i]+=2
print(arr[n])