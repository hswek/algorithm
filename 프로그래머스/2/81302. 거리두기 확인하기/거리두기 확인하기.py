def check_around(i,j,place):
    arr=[[1,0],[0,-1],[-1,0],[0,1]]
    for dx,dy in arr:
        nx,ny=i+dx,j+dy
        if nx>=5 or ny>=5 or nx<0 or ny<0:
            continue
        if place[nx][ny]=='P':
            return False
    for dx,dy in arr:
        nx,ny=i+dx*2,j+dy*2
        nx2,ny2=i+dx,j+dy
        if nx>=5 or ny>=5 or nx<0 or ny<0:
            continue
        if place[nx][ny]=='P' and place[nx2][ny2]!='X':
            return False
    arr=[[1,1],[1,-1],[-1,1],[-1,-1]]
    for dx,dy in arr:
        nx,ny=i+dx,j+dy
        if nx>=5 or ny>=5 or nx<0 or ny<0:
            continue
        if place[nx][ny]=='P' and (place[nx][j]!='X' or place[i][ny]!='X'):
            return False
    return True
def check_true(place):
    for i in range(5):
        for j in range(5):
            if place[i][j]=='P':
                if check_around(i,j,place)==False:      
                    return 0
    return 1
def solution(places):
    answer = []
    for place in places:
        answer.append(check_true(place))
    return answer