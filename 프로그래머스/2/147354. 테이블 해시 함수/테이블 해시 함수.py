def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x: [x[col-1],-x[0]])
    #print(data)
    s=0
    for i in range(row_begin-1,row_end):
        tmp=0
        for a in data[i]:
            tmp+=a%(i+1)

        s=s^tmp
    return s