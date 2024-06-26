from collections import deque
def solution(queue1, queue2):
    answer = 0
    d1=deque(queue1)
    d2=deque(queue2)
    idx1=0
    idx2=0
    s1=sum(queue1)
    s2=sum(queue2)
    l=len(queue1)+len(queue2)
    while idx1<len(d1) or idx2<len(d2):
        #print(d1,d2)
        #print(s1,s2)
        if s1==s2:
            return answer
        if idx1<l*2 and s1>s2:
            idx1+=1
            d2.append(d1.popleft())
            answer+=1
            s1-=d2[-1]
            s2+=d2[-1]
        elif idx2<l*2 and s1<s2:
            idx2+=1
            d1.append(d2.popleft())
            answer+=1
            s2-=d1[-1]
            s1+=d1[-1]
        else:
            break
    return -1