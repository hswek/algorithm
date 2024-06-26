from collections import deque
def solution(card1, card2, goal):
    card1=deque(card1)
    card2=deque(card2)
    is_true=True
    for i in goal:
    
        if len(card1)!= 0 and i== card1[0]:
            card1.popleft()
        elif len(card2)!= 0 and i==card2[0]:
            card2.popleft()
        else:
            is_true=False
    if is_true:
        return 'Yes'
    else:
        return 'No'
    answer = ''
    return answer