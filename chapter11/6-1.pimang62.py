'''
[무지의 먹방 라이브]
greedy !!
idea) 음식 시간이 적은 것 부터 k를 깎아 나감
ex. k = 5,
 -> 2번 음식 1초, 3번 음식 2초, 1번 음식 2초 먹다가 들킴!
but. 모두 0이 되면 -1 return
'''

import heapq

'''
def solution(food_times, k):

    q = []
    for num, time in enumerate(food_times):
        heapq.heappush(q, (time, num))

    while q:
'''

import heapq

def solution(food_times, k):
    
    if sum(food_times) <= k:
        return -1
    
    data = []
    for idx, time in enumerate(food_times):
        data.append((time, idx+1))
    
    data.sort()

    count = 0
    for info in data:
        t, i = info
        
    
'''
    while q :

    for info in data:
        t, i = info











    for _ in range(k):
        for info in data:
            t, i = info
            t -= 1
            if t == 0:
                continue
    return i+1
'''    
print(solution(food_times=[3, 1, 2], k = 5))
    
        

        
