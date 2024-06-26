from itertools import permutations,combinations_with_replacement 
def is_true(arr,n,idx):
    for i in range(idx):
        if arr[i]==arr[idx] or abs(arr[i]-arr[idx])==idx-i:
            return False
    return True
def dfs(arr,a,idx,n):
    if idx==n:
        return 1
    result=0
    for i in range(len(arr)):
        a[idx]=arr[i]
        
        if is_true(a,n,idx)==True:
            tmp=arr[i]
            arr.pop(i)
            result+=dfs(arr,a,idx+1,n)
            arr.insert(i,tmp)
    return result
def solution(n):
    arr=list(range(n))
    answer = dfs(arr,[-99]*n,0,n)
    return answer