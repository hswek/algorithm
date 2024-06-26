def solution(wallpaper):
    answer = []
    min_x=999999999999
    min_y=999999999999
    max_x=-1
    max_y=-1
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j]=='#':
                if min_x>i:
                    min_x=i
                if min_y>j:
                    min_y=j
                if max_x<i:
                    max_x=i
                if max_y<j:
                    max_y=j
    answer=[min_x,min_y,max_x+1,max_y+1]
    return answer