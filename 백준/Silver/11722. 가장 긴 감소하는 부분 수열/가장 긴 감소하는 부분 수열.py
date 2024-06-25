import sys
n=int(input())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
cache=[-1]*1101
def longest_arr(arr,pos):
    global n
    if cache[pos+1]!=-1:
        return cache[pos+1]
    
    result=1
    s=0
    if pos==n-1:
        return 1
    for i in range(pos+1,n):
        if pos==-1 or arr[pos]>arr[i]:
            s=max(s,longest_arr(arr,i))
    result+=s
    cache[pos+1]=result
    return result

print(longest_arr(arr,-1)-1)

    