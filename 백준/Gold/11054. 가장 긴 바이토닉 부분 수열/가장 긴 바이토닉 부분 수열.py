import sys
a=int(input())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
cache=[-1]*1101
def longest_arr(arr,pos,n):
    if cache[pos+1]!=-1:
        return cache[pos+1]
    
    result=1
    s=0
    if pos==n-1:
        return 1
    for i in range(pos+1,n):
        if pos==-1 or arr[pos]<arr[i]:
            s=max(s,longest_arr(arr,i,n))
    result+=s
    cache[pos+1]=result
    return result

#pos를 포함한, pos이후의 최대 감소하는 배열 길이 return
def shortest_arr(arr,pos,n):
    if cache[pos+1]!=-1:
        return cache[pos+1]
    
    result=1
    s=0
    if pos==n-1:
        return 1
    for i in range(pos+1,n):
        if pos==-1 or arr[pos]>arr[i]:
            s=max(s,shortest_arr(arr,i,n))
    result+=s
    cache[pos+1]=result
    return result

def bitonic(arr):
    max_len=0
    if len(arr)==1:
        return 1
    for i in range(1,len(arr)):
        global cache
        cache=[-1]*1101
        tmp=longest_arr(arr[:i],-1,i)-1
        cache=[-1]*1101
        tmp+=shortest_arr(arr,i-1,len(arr))-1
        max_len=max(max_len,tmp)
        #print(longest_arr(arr[:i],-1,len(arr[:i])),shortest_arr(arr,i-1,len(arr)),i)
    return max_len
print(bitonic(arr))

    