import sys
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
blue=0
white=0
def recursive(x1,y1,x2,y2):
    global blue,white

    #print('x1:%d,y1:%d,x2:%d,y2:%d'%(x1,y1,x2,y2))
    if x1+1==(x2):
        if arr[y1][x1]==1:
            blue+=1
        else:
            white+=1
        return
    tmp=[row[x1:x2] for row in arr[y1:y2]]
    s=0
    for i in tmp:
        s+=sum(i)
    #print(s)
    if s==(x2-x1)**2 or s==0:
        if s==0:
            white+=1
        else:
            blue+=1
        return
    mid_x=(x1+x2)//2
    mid_y=(y1+y2)//2
    #rint(x1,mid_x,x2)
    #rint(y1,mid_y,y2)
    recursive(x1,y1,mid_x,mid_y)
    recursive(mid_x,y1,x2,mid_y)
    recursive(x1,mid_y,mid_x,y2)
    recursive(mid_x,mid_y,x2,y2)
recursive(0,0,n,n)
print(white)
print(blue)

    
