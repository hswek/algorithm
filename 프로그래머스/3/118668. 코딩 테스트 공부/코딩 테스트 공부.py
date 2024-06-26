def rec(alp,cop,g1,g2,problems,cache):
    if alp>=g1 and cop>=g2:
        return 0
    if cache[min(g1,alp)][min(g2,cop)]!=-1:
        return cache[min(g1,alp)][min(g2,cop)]
    result=999999999999
    for n_al,n_co,al,co,t in problems:
        if alp>=n_al and n_co<=cop:
            if (al==0 and cop>=g2) or (co==0 and alp>=g1) or (al==0 and co==0):
                continue
                
            result=min(result,rec(alp+al,cop+co,g1,g2,problems,cache)+t)
    cache[min(g1,alp)][min(g2,cop)]=result
    return result
import sys        
def solution(alp, cop, problems):
    answer = 0
    sys.setrecursionlimit(10**6)
    problems.append([0,0,1,0,1])
    problems.append([0,0,0,1,1])
    g1=0
    g2=0
    for a,b,c,d,e in problems:
        g1=max(g1,a)
        g2=max(g2,b)
    cache=[[-1]*(g2+11) for i in range(g1+11)]
    answer=rec(alp,cop,g1,g2,problems,cache)
    
    
    
    return answer