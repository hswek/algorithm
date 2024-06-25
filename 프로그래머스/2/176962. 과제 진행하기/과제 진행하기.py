from collections import deque

def solution(plans):
    answer = []
    for i in range(len(plans)):
        a,b,c=plans[i]
        plans[i]=[a,int(b[:2])*60+int(b[3:5]),int(c)]
    plans.sort(key=lambda x:x[1])
    d=deque()
    now=plans[0][0]
    time=plans[0][1]
    rest=plans[0][2]
    for a,b,c in plans[1:]:
        if b-time< rest:
            #print(now,time,rest,a,b,c,1)
            d.appendleft([now,rest-(b-time)])
            time=b
            rest=c
            now=a
        elif b-time==rest:
            #print(now,time,rest,a,b,c,1)
            answer.append(now)
            rest=c
            now=a
            time=b
        else:
            #print(now,time,rest,a,b,c,1)
            answer.append(now)
            time=time+rest
            while len(d)!=0:
                now,new_rest=d[0]
                d.popleft()
                if (b-time) < new_rest:
                    new_rest=new_rest-(b-time)
                    time=b
                    d.appendleft([now,new_rest])
                    break
                elif (b-time) == new_rest:
                
                    answer.append(now)
                    break
                else:
                    time=time+new_rest
                    answer.append(now)
            now=a
            time=b
            rest=c
    answer.append(now)
    for i in d:
        answer.append(i[0])
                
            
        
    return answer