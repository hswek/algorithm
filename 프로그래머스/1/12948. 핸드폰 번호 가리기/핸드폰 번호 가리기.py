def solution(phone_number):
    answer = ''
    s='*'* (len(phone_number)-4)+phone_number[-4:]
    return s