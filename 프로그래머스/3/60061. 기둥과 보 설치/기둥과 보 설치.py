def check(arr,x,y,a):
    if a==0:
        if ( arr[x][y+1][0]==1 and check_good(arr,x,y+1,0)==False ) or (arr[x][y+1][1]==1 and check_good(arr,x,y+1,1)==False) or (x!=0 and arr[x-1][y+1][1]==1 and check_good(arr,x-1,y+1,1)==False):
            return False
    if a==1:
        if (arr[x][y][0]==1 and check_good(arr,x,y,0)==False) or (arr[x+1][y][0]==1 and check_good(arr,x+1,y,0)==False) or (arr[x+1][y][1]==1 and check_good(arr,x+1,y,1)==False) or (x!=0 and arr[x-1][y][1]==1 and check_good(arr,x-1,y,1)==False):
            return False
    return True
def check_good(arr,x,y,a):
    if a==0:
        if y==0:
            return True
        if arr[x][y-1][0]==1 or arr[x][y][1]==1 or (x>=1 and arr[x-1][y][1]==1):
            return True
    if a==1:
        if arr[x][y-1][0]==1 or arr[x+1][y-1][0]==1 or (x>=1 and x!=len(arr)-2 and arr[x-1][y][1]==1 and arr[x+1][y][1]==1):
            return True
    return False
def solution(n, build_frame):
    answer = []
    arr=[[[0]*2 for i in range(n+1)] for i in range(n+1)]
    for x,y,a,b in build_frame:
        if b==0:
            arr[x][y][a]=0
            if check(arr,x,y,a)==False:
                arr[x][y][a]=1
                continue
        else:
            arr[x][y][a]=1
            if check_good(arr,x,y,a)==False:
                arr[x][y][a]=0
    for i in range(n+1):
        for j in range(n+1):
            for z in range(2):
                if arr[i][j][z]==1:
                    answer.append([i,j,z])
    answer.sort()
    return answer