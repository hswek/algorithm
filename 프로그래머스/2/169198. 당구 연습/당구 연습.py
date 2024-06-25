def get_length(m,n,x,y,ballx,bally):
    result=9999999999999999999999999
    if not(bally>y and ballx==x):
        tmp= (x-ballx)**2+ (n*2-bally-y)**2
        result=min(result,tmp)
    if not(bally<y and ballx==x):
        tmp= (x-ballx)**2+ (-bally-y)**2
        result=min(result,tmp)
    if not(ballx>x and bally==y):
        tmp= (y-bally)**2+ (m*2-ballx-x)**2
        result=min(result,tmp)
    if not(ballx<x and bally==y):
        tmp= (y-bally)**2+ (-ballx-x)**2
        result=min(result,tmp)
    return result
def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        answer.append(get_length(m,n,startX,startY,ball[0],ball[1]))
    return answer