import sys
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
arr.sort()

cache=[-1]*1101
def longest_arr(arr,pos,n):
    if cache[pos+1]!=-1:
        return cache[pos+1]

    result=1
    s=0
    if pos==n-1:
        return 1
    for i in range(pos+1,n):
        if pos==-1 or arr[pos][1]<arr[i][1]:
            s=max(s,longest_arr(arr,i,n))
    result+=s
    cache[pos+1]=result
    return result

print(n+1-longest_arr(arr,-1,n))

