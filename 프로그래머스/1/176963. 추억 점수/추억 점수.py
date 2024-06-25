def solution(name, yearning, photo):
    answer = []
    d={}
    for i in range(len(name)): 
        d[name[i]]=yearning[i]
    for i in photo:
        result=0
        for j in i:
            if j in d:
                
                result+=d[j]
        
        answer.append(result)
    return answer