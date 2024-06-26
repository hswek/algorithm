from bisect import bisect_left
def get_query_result(query):
    global lang_d,what_d,year_d,soal_d,score_d,pre_query_d
    lang,what,year,soal=query.split(' and ')
    soal,score=soal.split()
    ss=lang+what+year+soal
    #print(pre_query_d[ss])
    return len(pre_query_d[ss])-bisect_left(pre_query_d[ss],int(score))
def solution(infos, querys):
    global lang_d,what_d,year_d,soal_d,score_d,pre_query_d
    answer = []
    lang_d={'java':set([]),'python':set([]),'cpp':set([]),'-':set([])}
    what_d={'backend':set([]),'frontend':set([]),'-':set([])}
    soal_d={'chicken':set([]),'pizza':set([]),'-':set([])}
    year_d={'junior':set([]),'senior':set([]),'-':set([])}
    score_d={}
    for i,info in enumerate(infos):
        lang,what,year,soal,score=info.split()
        lang_d[lang].add(i)
        what_d[what].add(i)
        year_d[year].add(i)
        soal_d[soal].add(i)
        lang_d['-'].add(i)
        what_d['-'].add(i)
        year_d['-'].add(i)
        soal_d['-'].add(i)
        score_d[i]=score
    pre_query_d={}
    for i in lang_d.keys():
        for j in what_d.keys():
            for z in year_d.keys():
                for o in soal_d.keys():
                    tmp=(lang_d[i]) & (what_d[j]) & (year_d[z]) & (soal_d[o])
                    s=[]
                    for ii in tmp:
                        s.append(int(score_d[ii]))
                    s.sort()
                    pre_query_d[i+j+z+o]=s
    for query in querys:
        answer.append(get_query_result(query))
    return answer