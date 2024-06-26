def solution(keymap, targets):
    answer = []
    d={}
    for i in keymap:
        for j in range(len(i)):
            if i[j] not in d:
                d[i[j]]=j+1
            elif d[i[j]] > j+1:
                d[i[j]]=j+1
    for i in targets:
        tmp_arr=0
        is_True=True
        for j in i:
            if j not in d:
                answer.append(-1)
                is_True=False
                break
            else:
                tmp_arr+=d[j]
        if is_True==True:
            answer.append(tmp_arr)
    return answer