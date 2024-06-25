def solution(players, callings):
    answer = []
    d={}
    for i in range(len(players)):
        d[players[i]]=i
    for i in callings:
        j=d[i]
        tmp=players[j]
        players[j]=players[j-1]
        players[j-1]=tmp
        
        tmp=d[players[j-1]]
        d[players[j-1]]=d[players[j]]
        d[players[j]]=tmp
                #swap(players[j],players[j-1])
    return players