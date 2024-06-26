from itertools import combinations
def solution(orders, course):
    answer = []
    d={}
    for num in course:
        d[num]={}
    for order in orders:
        for num in course:
            if num>len(order):
                break
            order=list(order)
            order.sort()
            order=''.join(order)
            subset_list=list(combinations(list(order),num))
            for subset in subset_list:
                subset=''.join(subset)
                if subset not in d[num]:
                    d[num][subset]=1
                else:
                    d[num][subset]+=1
    for d2 in d.values():
        arr=list(d2.items())
        #print(arr)
        if len(arr)==0:
            continue
        arr.sort(key=lambda x:-x[1])
        #print(arr)
        max_num=arr[0][1]
        if max_num==1:
            continue
        for a,b in arr:
            if b==max_num:
                answer.append(a)
    answer.sort()
    return answer