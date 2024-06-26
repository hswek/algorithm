from itertools import combinations
import sys
def solution(a):
    sys.setrecursionlimit(10**6)
    row,col=len(a),len(a[0])
    col_ones=[0]*col
    for i in range(col):
        s=0
        for j in range(row):
            col_ones[i]+=a[j][i] 
    comb=[[0]*301 for i in range(301)]
    cache={}
    for i in range(301):
        for j in range(301):
            if j == 0:
                comb[i][j] = 1
            elif i == j:
                comb[i][j] = 1
            else:
                comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) %(10**7+19)

    #c열에서 짝수행이 even개인 경우의 수
    def rec(c,even):
        if c==0:
            if row-even==col_ones[0]:
                return comb[row][col_ones[0]]
            return 0
        s=0
        ss=str(c)+"_"+str(even)
        if ss in cache:
            return cache[ss]
        for prev_even in range(row+1):
            now_even=(prev_even+col_ones[c]-even)
            if now_even%2!=0 :
                continue
            now_even=now_even//2
            if now_even<0 or now_even>prev_even or now_even>col_ones[c]:
                continue
            s+=comb[row-prev_even][col_ones[c]-now_even] *comb[prev_even][now_even] * rec(c-1,prev_even)
            s=s%(10**7+19)
        cache[ss]=s%(10**7+19)
        return cache[ss]
    return rec(col-1,row) %(10**7+19)