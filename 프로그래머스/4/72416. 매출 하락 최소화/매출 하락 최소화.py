
def solution(sales, links):
    answer = 0
    n=len(sales)
    sales.insert(0,0)
    arr=[[] for _ in range(n+1)]
    for parent,child in links:
        arr[parent].append(child)
    cache={}
    def rec(root,is_root_colored):  
        ss=str(root)+"_"+str(is_root_colored)
        if ss in cache:
            return cache[ss]
        if len(arr[root])==0:
            return 0
        if is_root_colored:
            result=0
            for child in arr[root]:
                result+=rec(child,False)
            cache[ss]=result
            return result
        else:
            result1=sales[root]
            for child in arr[root]:
                result1+=rec(child,False)
            result_arr=[result1]
            tmp=0
            for colored_child in arr[root]:
                tmp=sales[colored_child]
                for child in arr[root]:
                    if child==colored_child:
                        tmp+=rec(child,True)
                    else:
                        tmp+=rec(child,False)
                result_arr.append(tmp)
            #print(root,result_arr)
            cache[ss]=min(result_arr)
            return min(result_arr)
    return rec(1,False)