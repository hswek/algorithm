def solution(s):
    answer = []
    zero=0
    num=0
    while True:
        tmp=''
        for i in s:
            if i=='1':
                tmp+=i
            else:
                zero+=1
        tmp=len(tmp)
        arr=[]
        while True:
            arr.append(str(tmp%2))
            tmp=tmp//2
            if tmp==0:
                break
        s=''.join(arr)
        num+=1
        if s=='1':
            break
                
    return [num,zero]