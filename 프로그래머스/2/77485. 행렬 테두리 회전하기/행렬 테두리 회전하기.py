def rotate(x,y,x_end,y_end,arr):
    #result=99999999999999999
    up_right=arr[x][y_end]
    down_right=arr[x_end][y_end]
    up_left=arr[x][y]
    down_left=arr[x_end][y]
    result=min([up_right,down_right,up_left,down_left])
    
    for i in range(y_end,y,-1):
        arr[x][i]=arr[x][i-1]
        result=min(result,arr[x][i-1])
    for i in range(y,y_end):
        arr[x_end][i]=arr[x_end][i+1]
        result=min(result,arr[x_end][i+1])
    for i in range(x_end,x,-1):
        arr[i][y_end]=arr[i-1][y_end]
        result=min(result,arr[i-1][y_end])
    for i in range(x,x_end):
        arr[i][y]=arr[i+1][y]
        result=min(result,arr[i+1][y])
    arr[x+1][y_end]=up_right
    arr[x_end][y_end-1]=down_right
    arr[x_end-1][y]=down_left
    return result
def solution(rows, columns, queries):
    answer = []
    arr=[[i for i in range(1+i*columns,1+i*columns+columns)] for i in range(rows)]
    #print(arr)
    for x,y,x2,y2 in queries:
        answer.append(rotate(x-1,y-1,x2-1,y2-1,arr))
    return answer