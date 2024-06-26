def rec(x,y,tri):
    global cache
    if y==len(tri):
        return 0
    if cache[x][y]!=-1:
        return cache[x][y]
    result=tri[y][x]+max(rec(x,y+1,tri),rec(x+1,y+1,tri))
    cache[x][y]=result
    return result
def solution(triangle):
    global cache
    cache=[[-1]*(len(triangle)+1) for i in range(len(triangle)+1)]
    answer = rec(0,0,triangle)
    return answer