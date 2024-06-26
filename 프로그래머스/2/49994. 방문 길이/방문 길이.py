def solution(dirs):
    answer = 0
    x,y=0,0
    f={}
    d={'U':[0,1],'D':[0,-1],'R':[1,0],'L':[-1,0]}
    idx=0
    for s in dirs:
        idx+=1
        nx=x+d[s][0]
        ny=y+d[s][1]
        if nx>=6 or nx<=-6 or ny>=6 or ny<=-6:
            continue
        if nx*100000000 + x*100000 + y*1000 + ny not in f:
            #print(s,idx)
            answer+=1
            f[nx*100000000 + x*100000 + y*1000 + ny]=True
            f[x*100000000 + nx*100000 + ny*1000 + y]=True
        x=nx
        y=ny
    return answer