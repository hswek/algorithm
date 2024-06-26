import datetime 
def solution(a, b):
    answer = ''
    arr = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    answer=arr[datetime.date(2016,a,b).weekday()]
    return answer