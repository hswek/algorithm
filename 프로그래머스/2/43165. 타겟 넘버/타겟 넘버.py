import sys
def dfs(numbers,target,idx,s):
    if idx==len(numbers):
        if s==target:
            return 1
        else:
            return 0
    return dfs(numbers,target,idx+1,s-numbers[idx])+ dfs(numbers,target,idx+1,s+numbers[idx])
def solution(numbers, target):
    sys.setrecursionlimit(10**6)
    answer =dfs(numbers,target,0,0)
        
    return answer