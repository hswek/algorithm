def go_query(n,m,queries,x,y):
    x_start=x
    y_start=y
    answer=0
    x_end=x
    y_end=y
    queries.reverse()
    for command,dx in queries:
        #print(x_start,x_end,y_start,y_end)
        if command==0:
            if y_start==0:
                y_end=min(y_end+dx,m-1)
            else:
                y_start=y_start+dx
                y_end=min(m-1,y_end+dx)
        if command==1:
            if y_end==m-1:
                y_start=max(0,y_start-dx)
            else:
                y_start=max(0,y_start-dx)
                y_end=y_end-dx
        if command==2:
            if x_start==0:
                x_end=min(x_end+dx,n-1)
            else:
                x_start=x_start+dx
                x_end=min(n-1,x_end+dx)
        if command==3:
            if x_end==n-1:
                x_start=max(0,x_start-dx)
            else:
                x_start=max(0,x_start-dx)
                x_end=x_end-dx
        #print(x_start,x_end,y_start,y_end)
        if y_start > m - 1 or y_end < 0 or x_start > n - 1 or x_end < 0:
            return 0
    return (x_end-x_start+1)*(y_end-y_start+1)
def solution(n, m, x, y, queries):
    answer = 0
    answer=go_query(n,m,queries,x,y)
    return answer