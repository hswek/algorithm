def get_length(n):
    tmp=0
    while True:
        tmp+=(n%2)
        n=n//2
        if n==0:
            break
    return tmp
def solution(n):
    answer = 0
    arr=[]
    s=get_length(n)
    while True:
        n=n+1
        if get_length(n)==s:
            return n

