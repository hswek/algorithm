def solution(park, routes):
    answer = []
    x=-1
    y=-1
    d={'N':[-1,0],'S':[1,0],'E':[0,1],'W':[0,-1]}
    len_x=len(park)
    len_y=len(park[0])
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j]=='S':
                x=i
                y=j
    for s in routes:
        direction=s.split()[0]
        how=int(s.split()[1])
        a=d[direction]
        nx=x
        ny=y
        is_true=True
        for i in range(1,how+1):
            nx=nx+a[0]
            ny=ny+a[1]
            if nx<0 or ny<0 or nx>=len_x or ny>=len_y or park[nx][ny]=='X' :
                is_true=False
                break
        if is_true==True:
            x=nx
            y=ny
    answer=[x,y]
    
    return answer