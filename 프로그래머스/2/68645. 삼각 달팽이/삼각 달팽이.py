def solution(n):
    arr = [[-1] *n for i in range(n)]
    x=-1 
    y=0
    now=1
    answer=[]
    for i in range(n):
        for j in range(i,n):
            if i%3==0:
                x+=1
            elif i%3==1:
                y+=1
            else:
                x-=1
                y-=1
            arr[x][y]=now
            now+=1
    for i in range(n):
        for j in range(i+1):
            answer.append(arr[i][j])
    return answer