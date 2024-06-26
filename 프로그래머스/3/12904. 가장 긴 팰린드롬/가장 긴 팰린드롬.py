import sys
sys.setrecursionlimit(7000000)
def palindrome(left, right, s, visit):
    global answer
    
    #visit[left][right]를 체크해줌으로써 중복 문자열 탐색을 방지한다
    if visit[left][right] == 1: return
    visit[left][right] = 1
    
    l, r = left, right
    #팰린드롬이라면 ck = True, 필린드롬이 아니라면 ck = False
    ck = True
    
	#팰린드롬인지 판별하기
    while l<=r:
    	#왼쪽 문자열과 오른쪽 문자열이 다른 경우, 팰린드롬 문자열이 아니다
        if s[l] != s[r]:
        	#left값을 오른쪽으로 한 칸 옮겨서 탐색
            if left+1 <= right: palindrome(left+1, right, s, visit)
            #right값을 왼쪽으로 한 칸 옮겨서 탐색
            if right-1 >= left: palindrome(left, right-1, s, visit)
            #팰린드롬이 아니므로 ck = False하고 while문을 나간다
            ck = False
            break
        #l은 오른쪽으로 한 칸, r은 왼쪽으로 한 칸 조정
        l+=1
        r-=1
    #팰린드롬이라면 해당 문자열의 길이와 answer을 비교하여 갱신
    if ck == True:
        cnt = right-left+1
        if answer < cnt: answer = cnt
            
def solution(s):
    global answer
    answer = 1
    visit = [[0]*len(s) for i in range(len(s))]
    palindrome(0, len(s)-1, s, visit)

    return answer