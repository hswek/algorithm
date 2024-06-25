pp=int(input())

def a(n):
    if n==0 or n==1:
        return
    if zero_list[n-1]==-1:
        a(n-1)
    if zero_list[n-2]==-1:
        a(n-2)
    zero_list[n]=zero_list[n-1]+zero_list[n-2]
    one_list[n]=one_list[n-1]+one_list[n-2]
for _ in range(pp):
    p=int(input())
    zero_list=[-1]*(p+2)
    one_list=[-1]*(p+2)
    zero_list[0]=1
    one_list[0]=0
    zero_list[1]=0
    one_list[1]=1
    if p>=2:
        a(p)
    print(zero_list[p],one_list[p])
    
