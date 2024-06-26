def solution(cookie):
    answer = 0
    for mid in range(len(cookie)-1):
        d={}
        left_sum=0
        for left in range(mid,-1,-1):
            left_sum+=cookie[left]
            d[left_sum]=True
        right_sum=0
        for right in range(mid+1,len(cookie)):
            right_sum+=cookie[right]
            if right_sum in d:
                answer=max(answer,right_sum)
    return answer