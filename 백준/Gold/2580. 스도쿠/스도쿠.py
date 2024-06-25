arr=[]
import time
import sys
for i in range(9):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
    
def print_arr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j],end=' ')
        print()
        
def is_good(arr):
    for i in range(9):
        tmp=[0]*10
        for j in range(9):
            if arr[i][j]==0:
                continue
            if tmp[arr[i][j]]==1:
                
                return False
            else:
                tmp[arr[i][j]]=1
    for i in range(9):
        tmp=[0]*10
        for j in range(9):
            if arr[j][i]==0:
                continue
            if tmp[arr[j][i]]==1:
                
                return False
            else:
                tmp[arr[j][i]]=1
    tmp2=[[0,3],[0,6],[0,0],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
    for x,y in tmp2:
        tmp=[0]*10
        for j in range(3):
            for z in range(3):
                if arr[x+j][y+z]==0:
                    continue
                if tmp[arr[x+j][y+z]]==1:
                    
                    return False
                else:
                    tmp[arr[x+j][y+z]]=1
    return True
    
def find_zero(arr):
    for i in range(9):
        for j in range(9):
            if arr[i][j]==0:
                return [i,j]
    return -1

def sdk(arr):

    #if is_good(arr)==False:
    #    return False
    xy=find_zero(arr)
    if xy==-1:
        if is_good(arr)!=False:
            print_arr(arr)
            return True
        return False
    tmp=[0]*10
    for j in range(9):
        tmp[arr[j][xy[1]]]=1
    x1=xy[0]//3*3
    x2=xy[1]//3*3
    for i in range(3):
        for j in range(3):
            tmp[arr[x1+i][x2+j]]=1

    for i in range(1,10):
        if i in arr[xy[0]] or tmp[i]==1:
            continue
        arr[xy[0]][xy[1]]=i
        if sdk(arr)==True:
            return True
    arr[xy[0]][xy[1]]=0
    return False
#s=time.time()
sdk(arr)
#print(time.time()-s)