def is_true(now):
    idx=0
    global d,skills
    for s in now:
        if s in d and skills[idx]==s:
            idx+=1
        elif s in d and skills[idx]!=s:
            return False
    return True
def solution(skill, skill_trees):
    global d,skills
    skills=skill
    answer = 0
    d={}
    for s in skill:
        d[s]=True
    for now in skill_trees:
        if is_true(now)==True:
            answer+=1
        

            
            
    return answer