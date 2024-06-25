from itertools import combinations 
def cal_winrate(a,b):
    a_case={}
    b_case={}
    win=0
    def dfs(l,origin,d):
        if len(l)==len(origin):
            tmp=0
            for j in range(len(l)):
                tmp+=origin[j][l[j]]
            if tmp not in d:
                d[tmp]=0
            d[tmp]+=1
            return
        for i in range(6):
            l.append(i)
            dfs(l,origin,d)
            l.pop()
    dfs([],a,a_case)
    dfs([],b,b_case)
    for a_what,a_nums in a_case.items():
        for b_what,b_nums in b_case.items():
            if a_what>b_what:
                win+=a_nums*b_nums
    return win
            
def solution(dice):
    answer = []
    max_num=0
    dice_len=len(dice)
    for a in list(combinations(range(dice_len),dice_len//2)):
        b=[]
        for i in range(dice_len):
            if i not in a:
                b.append(i)
        a_dice=[]
        for i in a:
            a_dice.append(dice[i])
        b_dice=[]
        for i in b:
            b_dice.append(dice[i])   
        result=cal_winrate(a_dice,b_dice)
        if max_num<result:
            answer=list(a)
            for i in range(len(answer)):
                answer[i]+=1
            max_num=result
    return answer