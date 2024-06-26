def update(r,c,val):
    r1,c1=parent[r][c]
    valarr[r1][c1]=val
def update2(val1,val2):
    for i in range(51):
        for j in range(51):
            if valarr[i][j]==val1:
                valarr[i][j]=val2
def merge(r1,c1,r2,c2):
    x1,y1=parent[r1][c1]
    x2,y2=parent[r2][c2]
    for i in range(51):
        for j in range(51):
            if parent[i][j][0]==x2 and parent[i][j][1]==y2:
                parent[i][j]=[x1,y1]
    if valarr[x1][y1]==None:
        valarr[x1][y1]=valarr[x2][y2]
def unmerge(r1,c1):
    x,y=parent[r1][c1]
    origin=valarr[x][y]
    for i in range(51):
        for j in range(51):
            if parent[i][j][0]==x and parent[i][j][1]==y:
                parent[i][j]=[i,j]
                valarr[i][j]=None
    valarr[r1][c1]=origin
def pri(r,c):
    global answer
    x,y=parent[r][c]
    if valarr[x][y]==None:
        answer.append('EMPTY')
    else:
        answer.append(valarr[x][y])
def solution(commands):
    global parent,answer,valarr
    answer = []
    parent=[ [ [i,j] for j in range(51)]  for i in range(51)]
    valarr=[ [ None for j in range(51)]  for i in range(51)]
    for c in commands:
        #print(c)
        arr=c.split()
        if arr[0]=='UPDATE':
            if len(arr)==4:
                t,r,c,val=arr
                r=int(r)
                c=int(c)
                update(r,c,val)
            if len(arr)==3:
                t,val1,val2=arr
                update2(val1,val2)
        if arr[0]=='MERGE':
            t,r1,c1,r2,c2=arr
            r1=int(r1)
            c1=int(c1)
            r2=int(r2)
            c2=int(c2)
            merge(r1,c1,r2,c2)
        if arr[0]=='PRINT':
            t,r,c=arr
            r=int(r)
            c=int(c)
            pri(r,c)
        if arr[0]=='UNMERGE':
            t,r,c=arr
            r=int(r)
            c=int(c)
            unmerge(r,c)
    return answer