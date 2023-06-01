

import heapq

def solution(food_times, k):

    if sum(food_times) <= k:
        return -1
    
    q = []
    for idx, time in enumerate(food_times):
        heapq.heappush(q, (time, idx+1))
    
    k_total = 0
    once = 0  # 직전에 다 먹은 시간 : 첫 번째 음식을 다 먹은 만큼 횟수만큼 차감해야 하기 때문 !
    length = len(food_times)
    while k_total <= k :
        
        k_prime = (q[0][0] - once) * length
        
        if k_total + k_prime > k :
            break

        once = heapq.heappop(q)[0]
        k_total += k_prime
        length -= 1

    # 인덱스 찾기
    i = (k - k_total) % length
    # 번호 순 정렬
    q = sorted(q, key = lambda x : x[1])
    return q[i][1]


print(solution(food_times=[3, 1, 2], k = 5))    # 1
print(solution(food_times=[3, 1, 2], k = 6))    # -1
print(solution(food_times=[8, 6, 4], k = 15))   # 2
    