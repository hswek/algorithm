def solution(number, k):
    answer = ''
    tmp=''
    now=0
    for num in number:
        while k!=0 and tmp!='' and now<num:
            tmp=tmp[:-1]
            k-=1
            if len(tmp)!=0:
                now=tmp[-1]
        tmp+=str(num)     
        now=num
    tmp=tmp[:len(tmp)-k]
    return tmp