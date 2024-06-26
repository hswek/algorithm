def solution(nums):
    answer = 0
    a={}
    for i in nums:
        if i not in a:
            a[i]=1
    arr=list(a.keys())
    answer=min(len(nums)//2,len(arr))
    return answer