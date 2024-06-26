def solution(citations):
    answer = 0
    for i in range(0,1000):
        num=0
        for ci in citations:
            if ci>=i:
                num+=1
        if num>=i:
            answer=i
    return answer