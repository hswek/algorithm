def solution(name):
    answer = 0
    cursur=0
    for i in range(len(name)):
        if name[i]=='A':
            continue
        tmp=min(abs(ord(name[i])-ord('A')),abs(ord('Z')-ord('A')+1-(ord(name[i])-ord('A'))))
        answer+=tmp
    max_a_length=0
    m=len(name)-1
    for i in range(len(name)):
        l=i+1
        while l<len(name):
            if name[l]=='A':
                l+=1
            else:
                break
        m=min([m,(i)*2+len(name)-l,(i)+(len(name)-l)*2])
    
            
    return answer+m