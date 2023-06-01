'''
*[무지의 먹방 라이브]
회전판에 먹어야 할 n개의 음식이 있습니다. 
각 음식에는 1부터 n까지의 번호가 붙어 있습니다.
1. 1번 음식부터 먹기 시작하여 회전판을 돌림 
2. 마지막 번호를 섭취한 후에는 다시 1번
 -> index == len(list), index = 0 변경
3. 음식 하나를 1초 동안 섭취 후 다음 음식 섭취
4. 회전판이 돌아가는데 걸리는 시간은 없다고 가정
Q. 무지가 먹방을 시작한 k초 후, 그 다음 먹어야 할 음식 번호는?

* [0, 0, 0, 1] 인데 i가 1번이라면 2번이 아닌 4번을 return해야 함!
'''

def solution(food_times, k):
    
    if sum(food_times) <= k:
            return -1
    
    i = 0
    # k초까지 반복
    for _ in range(k):
       
        if food_times[i] == 0:
            i = (i+1) % len(food_times)
    
        food_times[i] -= 1

        i = (i+1) % len(food_times)
    
    for i in range(i, len(food_times)+1):
        if food_times[i] != 0:
            return i+1 

print(solution(food_times=[3, 1, 2], k = 5))    # 1
print(solution(food_times=[3, 1, 2], k = 6))    # -1
print(solution(food_times=[8, 6, 4], k = 15))   # 2


