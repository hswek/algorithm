def solution(n):
    answer = 0
    n=str(n)
    n=list(n)
    n.sort(reverse=True)
    s=''
    for i in n:
        s+=i
    s=int(s)
   # print(n)
    return s