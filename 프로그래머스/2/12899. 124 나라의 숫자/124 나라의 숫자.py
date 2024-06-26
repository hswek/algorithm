def solution(n):
    answer = ''
    arr=[]
    while True:
        tmp=n%3
        if tmp==0:
            tmp=4
            n=n//3-1
        else:
            n=n//3
        arr.append(str(tmp))
        if n==0:
            break
    arr.reverse()
    
    return ''.join(arr)