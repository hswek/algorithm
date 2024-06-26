from collections import deque
def solution(c_size, cities):
    answer = 0
    cache=deque([])
    for city in cities:
        if city.lower() in cache:
            cache=list(cache)
            cache.remove(city.lower())
            cache=deque(cache)
            cache.append(city.lower())
            answer+=1
        else:
            
            cache.append(city.lower())
            if len(cache)>c_size:
                cache.popleft()
            answer+=5
    return answer