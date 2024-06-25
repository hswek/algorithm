pp=int(input())

def a(n):
    x1=0
    x2=0
    x3=0
    if n>3:
        if num_list[n-3]!=-1:
            x1=num_list[n-3]
        else:
            a(n-3)
            x1=num_list[n-3]
    if n>2:
        if num_list[n-2]!=-1:
            x2=num_list[n-2]
        else:
            a(n-2)
            x2=num_list[n-2]
    if n>1:
        if num_list[n-1]!=-1:
            x3=num_list[n-1]
        else:
            a(n-1)
            x3=num_list[n-1]
    num_list[n]=x1+x2+x3

for _ in range(pp):
    p=int(input())
    num_list=[-1]*(p+4)
    num_list[1]=1
    num_list[2]=2
    num_list[3]=4
    if p>=4:
        a(p)
    print(num_list[p])
    