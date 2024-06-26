def dfs(n,arr,who,visit):
    result=0
    for i in arr[who]:
        if i not in visit:
            visit.append(i)
            result+=dfs(n,arr,i,visit)+1
    return result
def solution(n, results):
    answer = 0
    win=[[] for i in range(n+1)]
    lose=[[] for i in range(n+1)]
    for w,l in results:
        win[w].append(l)
        lose[l].append(w)
    for i in range(1,n+1):
        #print(i,dfs(win,i),dfs(lose,i))
        #print(i)
        if dfs('win',win,i,[])+dfs('lose',lose,i,[])==n-1:
            answer+=1
    
    return answer