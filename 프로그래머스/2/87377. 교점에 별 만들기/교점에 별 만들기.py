def solution(line):
    answer = []
    s=[]
    for i in range(len(line)):
        for j in range(i+1,len(line)):

            a,b,e=line[i]
            c,d,f=line[j]
            if (a*d-b*c)==0:
                continue
            x=(b*f - e*d)/(a*d-b*c)
            y=(e*c-a*f)/(a*d-b*c)
            if x==int(x) and y==int(y):
                s.append([int(x),int(y)])
    x_min,x_max,y_min,y_max=min(s,key=lambda x:x[0])[0],max(s,key=lambda x:x[0])[0],min(s,key=lambda x:x[1])[1],max(s,key=lambda x:x[1])[1]
    print(s)
    #print(x_min,x_max,y_min,y_max)
    arr=[['.']*(x_max-x_min+1) for i in range(y_max-y_min+1)]
    for x,y in s:
        arr[y-y_min][x-x_min]='*'
    for i in range(len(arr)):
    
        arr[i]=''.join(arr[i])
    arr.reverse()
    return arr