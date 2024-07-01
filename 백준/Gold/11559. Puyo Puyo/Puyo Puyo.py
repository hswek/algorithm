import sys

arr=[]
for i in range(12):
    arr.append(list(sys.stdin.readline().rstrip()))
def dfs(x,y,color):
    global visit
    dx=[1,0,-1,0]
    visit[x][y]=True
    dy=[0,-1,0,1]
    result=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=12 or ny>=6 or visit[nx][ny]==True or arr[nx][ny]=='.':
            continue
        if arr[nx][ny]==color:
            result+=dfs(nx,ny,color)
    return result
def erase(x,y,color):
    global visit
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]
    visit[x][y]=True
    arr[x][y]='.'
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=12 or ny>=6 or visit[nx][ny]==True or arr[nx][ny]!=color:
            continue
        erase(nx,ny,color)
def not_upper(i,j):
    for i in range(i-1,-1,-1):
        if arr[i][j]!='.':
            return True
    return False
def fall():
    for j in range(6):
        how_fall=0
        i=11
        while i!=-1:
            if arr[i][j]=='.' and not_upper(i,j):
                for z in range(i,0,-1):
                    arr[z][j]=arr[z-1][j]
                arr[0][j]='.'
                continue
            i-=1
def print_arr(a):
    for i in a:
        print(i)
is_break=True
ans=0
while is_break:
    is_break=False
    for i in range(12):
        for j in range(6):
            if arr[i][j]!=".":
                visit=[[False]*6 for i in range(12)]
                if dfs(i,j,arr[i][j])>=4:
                    is_break=True
                    visit=[[False]*6 for i in range(12)]
                    erase(i,j,arr[i][j])
    fall()
    if is_break:
        ans+=1
                
print(ans)