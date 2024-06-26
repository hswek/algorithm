from collections import deque
def solution(s):
    answer = 0
    d=deque()
    
    for i in range(1,len(s)+1):
        d=deque()
        a=True
        for j in s:
            #print(i,d,j)
            if j=='(':
                d.append(j)
            elif j=='[':
                d.append(j)
            elif j=='{':
                d.append(j)
            elif j==')':
                if len(d)==0 or d[-1]!='(':
                    a=False
                    break
                else:
                    d.pop()
            elif j==']':
                if len(d)==0 or d[-1]!='[':
                    #print(d[-1])
                    a=False
                    break
                else:
                    d.pop()
            elif j=='}':
                if len(d)==0 or d[-1]!='{':
                    a=False
                    break
                else:
                    d.pop()
        if len(d)!=0:
            a=False
        if a==True:
            answer+=1
        s=s[1:]+s[:1]
    return answer