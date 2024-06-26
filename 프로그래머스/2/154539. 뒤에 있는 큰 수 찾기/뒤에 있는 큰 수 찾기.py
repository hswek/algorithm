from collections import deque
def solution(numbers):
    answer = [-1] * len(numbers)
    d=deque([[numbers[0],0]])
    for idx in range(1,len(numbers)):
        #print(d[-1])
        if d[-1][0]>= numbers[idx]:
            d.append([numbers[idx],idx])
        else:
            while len(d):
                if d[-1][0]>=numbers[idx]:
                    break
                else:
                    a,b=d[-1]
                    answer[b]=numbers[idx]
                    d.pop()
            d.append([numbers[idx],idx])
                    
    return answer