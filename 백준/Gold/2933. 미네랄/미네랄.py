import sys
import heapq
import copy

r,c=map(int,sys.stdin.readline().split())
arr=[]
for i in range(r):
    arr.append(list(sys.stdin.readline().rstrip()))
a=int(sys.stdin.readline().rstrip())
sys.setrecursionlimit(10**4)
def erase(arr,turn,height):
    global c
    if turn==0:
        col=0
        end=c
        add=1
    else:
        col=c-1
        end=-1
        add=-1
    for i in range(col,end,add):
        if arr[height][i]=='x':
            arr[height][i]='.'
            return True
    return False
turn=0
def dfs(arr,visit,x,y):
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]
    global r,c
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if nx<0 or ny<0 or nx>=r or ny>=c or arr[nx][ny]=='.' or visit[nx][ny]==1:
            continue
        visit[nx][ny]=1
        dfs(arr,visit,nx,ny)

def check_is_ground(arr):
    global r,c
    height=r-1
    visit=[[0]*c for i in range(r)]
    for i in range(c):
        if arr[height][i]=='x':
            dfs(arr,visit,height,i)
    return visit
def make_next_block(arr,visit,x,y,new_arr):
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]
    new_arr[x+1][y]=1
    arr[x][y]='.'
    global r,c
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if nx<0 or ny<0 or nx>=r or ny>=c or arr[nx][ny]=='.' or visit[nx][ny]==1:
            continue
        visit[nx][ny]=1
        make_next_block(arr,visit,nx,ny,new_arr)
def paste(arr,new_arr):
    global r,c
    result=True
    for i in range(r):
        for j in range(c):
            if new_arr[i][j]==1:
                arr[i][j]='x'
                if i==r-1 or (i!=r-1 and arr[i+1][j]=='x'):
                    result=False
    if result==True:
        for i in range(r):
            for j in range(c):
                if new_arr[i][j]==1:
                    arr[i][j]='.'
        next_arr=[[0]*c for i in range(r)]
        for i in range(1,r):
            for j in range(c):
                next_arr[i][j]=new_arr[i-1][j]
        new_arr=next_arr
    return result,new_arr
def go_gravity(arr,visit):
    for next_height in range(r-2,-1,-1):
        for i in range(c):
            if arr[next_height][i]=='x' and visit[next_height][i]==0:
                new_arr=[[0]*c for i in range(r)]
                make_next_block(arr,copy.deepcopy(visit),next_height,i,new_arr)
                result,new_arr=paste(arr,new_arr)
                return result,new_arr
    return False,[]

def print_arr(arr):
    global c
    for i in arr:
        if len(i)!=c:
            return
        print(''.join(i).rstrip())      
height_list=list(map(int,sys.stdin.readline().split()))
for height in height_list:
    height=r-height
    reuslt=erase(arr,turn,height)
    if reuslt==False:
        turn+=1
        turn=turn%2
        continue
    visit=check_is_ground(arr)
    is_true,new_arr=go_gravity(arr,visit)
    while is_true:
        is_true,new_arr=paste(arr,new_arr)
    
    visit=check_is_ground(arr)
    is_true,new_arr=go_gravity(arr,visit)
    while is_true:
        is_true,new_arr=paste(arr,new_arr)
    turn+=1
    turn=turn%2
print_arr(arr)
    

    