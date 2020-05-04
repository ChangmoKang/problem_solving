from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    time = 0
    cache = deque([], maxlen=cacheSize)
    
    for city in cities:
        city = city.lower()
        
        if city not in cache:
            time += 5
            cache.append(city)
        else:
            time += 1
            cache.remove(city)
            cache.append(city)

    return time
