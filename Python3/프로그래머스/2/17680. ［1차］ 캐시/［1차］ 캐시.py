def solution(cacheSize, cities):
    cache = []
    answer = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            cache.append(city)
            answer += 5
            if len(cache) > cacheSize:
                del cache[0]
    return answer