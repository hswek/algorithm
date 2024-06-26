def go_light(i,j,z,grid):
    global dis_arr,turn_left,turn_right,visit
    
    if visit[i][j][z]!=-1:
        return 0
    visit[i][j][z]=1
    tmp={0:'left',1:'right',2:'down',3:'up'}
    tmp2={}
    for key,val in tmp.items():
        tmp2[val]=key
    #print(i,j,tmp[z],grid[i][j])
    if grid[i][j]=='L':
        nd=turn_left[tmp[z]]
        ni=i+dis_arr[nd][0]
        nj=j+dis_arr[nd][1]
    if grid[i][j]=='R':
        nd=turn_right[tmp[z]]
        ni=i+dis_arr[nd][0]
        nj=j+dis_arr[nd][1]
    if grid[i][j]=='S':
        nd=tmp[z]
        ni=i+dis_arr[nd][0]
        nj=j+dis_arr[nd][1]
    if ni>=len(grid):
        ni=0
    if ni<0:
        ni=len(grid)-1
    if nj>=len(grid[0]):
        nj=0
    if nj<0:
        nj=len(grid[0])-1  
    return 1+go_light(ni,nj,tmp2[nd],grid)
import sys
def solution(grid):
    sys.setrecursionlimit(10**6)
    global dis_arr,turn_left,turn_right,visit
    answer = []
    dis_arr={'down':[-1,0],
    'up':[1,0],
    'right':[0,1],
    'left':[0,-1]}
    turn_left={'left':'down','down':'right','right':'up','up':'left'}
    turn_right={'left':'up','up':'right','right':'down','down':'left'}
    visit=[[[-1]*4 for i in range(len(grid[0]))] for j in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for z in range(4):
                #print(visit[i][j][z])
                if visit[i][j][z]==-1:            
                    answer.append(go_light(i,j,z,grid))
                    #print()
    answer.sort()
    return answer