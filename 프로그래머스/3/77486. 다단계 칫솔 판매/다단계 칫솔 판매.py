def solution(enroll, parent, seller, amount):
    answer = []
    str_to_int={}
    for i in range(len(enroll)):
        str_to_int[enroll[i]]=i
    int_to_str={}
    for key,val in str_to_int.items():
        int_to_str[val]=key
    arr=[0]*len(enroll)
    for i in range(len(amount)):
        sell,am=seller[i],amount[i]
        arr[str_to_int[sell]]+=am*90
        am=am*10
        p=sell
        while True:
            p=parent[str_to_int[p]]
            if p=='-':
                break  
            arr[str_to_int[p]]+=am-am//10
            am=am//10
            if am==0:
                break

    return arr