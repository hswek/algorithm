from itertools import permutations
def solution(expression):
    answer = 0
    arr2=['*','+','-']
    arr=list(permutations(arr2,3))
    tmp=''
    b=[]
    m=0
    for s in expression:
        if s not in arr2:
            tmp+=s
        else:
            b.append(int(tmp))
            b.append(s)
            tmp=''
    b.append(int(tmp))
    c=b.copy()
    #print(b)
    for a in arr:
        for s in a:
            tmp_arr=[]
            idx=0
            while idx<len(b):
                if b[idx]!=s:
                    tmp_arr.append(b[idx])
                else:
                    if s=='*':
                        tmp_arr[-1]=tmp_arr[-1] * b[idx+1]
                    if s=='+':
                        tmp_arr[-1]=tmp_arr[-1] + b[idx+1]
                    if s=='-':
                        tmp_arr[-1]=tmp_arr[-1] - b[idx+1]
                    idx+=1
                idx+=1
            b=tmp_arr
        m=max(m,abs(b[0]))
        b=c
    return m