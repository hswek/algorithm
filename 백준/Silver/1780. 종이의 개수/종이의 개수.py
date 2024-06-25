import sys
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
minus=0
zero=0
plus=0
def recursive(x1,y1,x2,y2):
    global minus,zero,plus

    #print('x1:%d,x2:%d,y1:%d,y2:%d'%(x1,x2,y1,y2))
    if x1+1==(x2):
        if arr[y1][x1]==-1:
            minus+=1
        elif arr[y1][x1]==0:
            zero+=1
        else:
            plus+=1
        return
    tmp=[row[x1:x2] for row in arr[y1:y2]]
    s=tmp[0][0]
    isTrue=True
    for i in tmp:
        for j in i:
            if j!=s:
                isTrue=False
    #print(s)
    if isTrue==True:
        if s==-1:
            minus+=1
        elif s==0:
            zero+=1
        else:
            plus+=1
        return
    plus_x=(x2-x1)//3
    plus_y=(y2-y1)//3

    for i in range(3):
        for j in range(3):
            recursive(x1+i*plus_x,y1+j*plus_y,x1+(i+1)*plus_x,y1+(j+1)*plus_y)

recursive(0,0,n,n)
print(minus)
print(zero)
print(plus)

    
