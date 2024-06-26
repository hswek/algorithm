def num_diff(s1,s2):
    if len(s1)!=len(s2):
        return 999
    result=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            result+=1
    return result
def dfs(now,target,visit,cache,words,begin):
    #print(words[now])
    if now!=-1 and words[now]==target:
        return 0
    if cache[now]!=-1:
        return cache[now]
    result=999999999999
    for i in range(len(words)):
        if now==i:
            continue
        if now==-1 and num_diff(begin,words[i])==1:
            visit[i]=1
            result=min(result,dfs(i,target,visit,cache,words,begin)+1)
            visit[i]=-1
        elif now!=-1 and visit[i]==-1 and num_diff(words[i],words[now])==1:
            visit[i]=1
            result=min(result,dfs(i,target,visit,cache,words,begin)+1)
            visit[i]=-1
        #if now==-1:
        #    print(result)
        #    print(num_diff(begin,words[i]),words[i])
    cache[now]=result
    return result
def solution(begin, target, words):
    answer = 0
    visit=[-1]*len(words)
    cache=[-1]*len(words)
    answer=dfs(-1,target,visit,cache,words,begin)
    if answer>=99999999999:
        answer=0
    return answer