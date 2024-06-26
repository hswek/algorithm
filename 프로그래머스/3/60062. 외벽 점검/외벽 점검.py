from itertools import permutations
def solution(n, weak, dist):
    answer = 0
    for i in range(len(weak)):
        weak.append(weak[i]+n)
    dist.sort()
    dist.reverse()
    for i in range(1,len(dist)+1):
        now=dist[:i]
        arr=list(permutations(now,len(now)))
        for a in arr:
            for s in range(len(weak)//2):
                nn=0
                ori=s
                for j in a:
                    if len(weak)<=s:
                        break
                    where=weak[s]+j
                    while s<len(weak):
                        if weak[s] <= where:
                            s+=1
                            nn+=1
                        else:
                            break
                #print(now,ori,s,nn)
                if nn>=len(weak)//2:
                    return i
    return -1
                    
                
            
    return answer