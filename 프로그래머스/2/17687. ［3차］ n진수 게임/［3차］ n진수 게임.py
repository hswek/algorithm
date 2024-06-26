def solution(n, t, m, p):
    answer = ''
    arr=[]
    for i in range(t):
        arr.append(m*i+p)
    now=0
    idx=1
    while True:
        tmp_arr=[]
        aa=now
        while True:
            tmp_arr.append(aa%n)
            aa=aa//n
            if aa==0:
                break
        tmp_arr.reverse()
        #print(now,tmp_arr)
        for num in tmp_arr:
            if idx in arr:
                print(idx,str(num))
                if num==10:
                    num='A'
                if num==11:
                    num='B'
                if num==12:
                    num='C'
                if num==13:
                    num='D'
                if num==14:
                    num='E'
                if num==15:
                    num='F'
                answer=answer+str(num)
            idx+=1
        if idx>arr[-1]:
            break
        now+=1
    return answer