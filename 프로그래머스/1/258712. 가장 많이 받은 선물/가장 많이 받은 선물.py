def solution(friends, gifts):
    answer = 0
    f2n={}
    n2f={}
    for i in range(len(friends)):
        n2f[i]=friends[i]
        f2n[friends[i]]=i
    l=len(friends)
    gift_mat=[[0]*l for _ in range(l)]
    for g in gifts:
        give,take=g.split()
        gift_mat[f2n[give]][f2n[take]]+=1
    new_gift_mat=[0]*l
    gift_value=[0]*l
    for i in range(l):
        gift_value[i]=sum(gift_mat[i])
    for j in range(l):
        for i in range(l):
            gift_value[j]-=gift_mat[i][j]
    for i in range(l):
        for j in range(i+1,l):
            if gift_mat[i][j]==gift_mat[j][i]:
                if gift_value[i]>gift_value[j]:
                    new_gift_mat[i]+=1
                elif gift_value[i]<gift_value[j]:
                    new_gift_mat[j]+=1
            elif gift_mat[i][j]>gift_mat[j][i]:
                new_gift_mat[i]+=1
            else:
                new_gift_mat[j]+=1
    for j in range(l):
        answer=max(answer,new_gift_mat[j])
        
    return answer