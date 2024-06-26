from itertools import permutations 

def solution(k, dungeons):
    arr2=list(permutations(dungeons,len(dungeons)))
    answer=0
    #print(arr2)
    for arr in arr2:
        now=k
        tmp=0
        #print(arr)
        for j in arr:
            if now< j[0]:
                answer=max(answer,tmp)
                break
            else:
                now=now-j[1]
                tmp+=1
                answer=max(answer,tmp)
        
    return answer