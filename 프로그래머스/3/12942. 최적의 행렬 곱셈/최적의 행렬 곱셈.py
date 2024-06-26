def rec(i,j,arr):
    global cache
    if cache[i][j]!=-1:
        return cache[i][j]
    if i==j:
        return [0,arr[i]]
    if i+1==j:
        return [arr[i][0]*arr[i][1]*arr[j][1],[arr[i][0],arr[j][1]]]
    result=999999999
    for z in range(i+1,j+1):
        a,b=rec(i,z-1,arr)
        c,d=rec(z,j,arr)
        e=b[0]*b[1]*d[1]
        if result>a+c+e:
            result=min(result,a+c+e)
            m_b=b
            m_d=d
    cache[i][j]=[result,[m_b[0],m_d[1]]]
    
    return cache[i][j]
def solution(arr):
    answer = 0
    global cache
    cache=[[-1]*(len(arr)+10) for i in range(len(arr)+10)]
    answer=rec(0,len(arr)-1,arr)[0]
    return answer