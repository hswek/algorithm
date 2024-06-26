def solution(answers):
    answer = []
    one=[1,2,3,4,5]
    two=[2,1,2,3,2,4,2,5]
    three=[3,3,1,1,2,2,4,4,5,5]
    win=[0,0,0]
    idx=0
    for arr in [one,two,three]:
        for i in range(len(answers)):
            if answers[i]==arr[i%len(arr)]:
                win[idx]+=1   
        idx+=1
    m=max(win)
    print(win)
    for i in range(len(win)):
        if m==win[i]:
            answer.append(i+1)
    return answer