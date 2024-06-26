def solution(lottos, win_nums):
    answer = 0
    zero=0
    l={6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    
    for i in lottos:
        if i==0:
            zero+=1
        else:
            if i in win_nums:
                answer+=1
                
    first=min(answer+zero,6)
    second=max(answer,1)
    answer=[l[first],l[second]]

    return answer