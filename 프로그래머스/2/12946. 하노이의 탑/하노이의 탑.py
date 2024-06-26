def rec(n,start,end,middle):
    global answer
    if n==0:
        return
    rec(n-1,start,middle,end)
    answer.append([start,end])
    rec(n-1,middle,end,start)
def solution(n):
    global answer
    answer = []
    rec(n,1,3,2)
    return answer