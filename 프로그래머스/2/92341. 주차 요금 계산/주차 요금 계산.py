import math
def solution(fees, records):
    answer = []
    i={}
    o={}
    ff={}
    for record in records:
        time,num,what=record.split()
        if what=='IN':
            i[num]=time
        else:
            i_time=i[num]
            o_time=time
            o_time=int(o_time.split(":")[0])*60+ int(o_time.split(":")[1])
            i_time=int(i_time.split(":")[0])*60+ int(i_time.split(":")[1])
            tmp=o_time-i_time
            if num not in ff:
                ff[num]=tmp
            else:
                ff[num]+=tmp
            del(i[num])
    for key,val in i.items():
        o[key]=['23:59',val]
    for key,val in o.items():
        o_time=val[0]
        i_time=val[1]
        o_time=int(o_time.split(":")[0])*60+ int(o_time.split(":")[1])
        i_time=int(i_time.split(":")[0])*60+ int(i_time.split(":")[1])
        tmp=o_time-i_time
        f= fees[1] + max(0,math.floor((tmp-fees[0])//fees[2])) * fees[3]
        if key not in ff:
            ff[key]=tmp
        else:
            ff[key]+=tmp
    for key,tmp in ff.items():
        
        f= fees[1] + max(0,math.ceil((tmp-fees[0])/fees[2])) * fees[3]
        #print(tmp,f,max(0,math.floor((tmp-fees[0])/fees[2])))
        ff[key]=f
    arr=list(ff.items())
    arr.sort()
    arr2=[i[1] for i in arr]
    return arr2