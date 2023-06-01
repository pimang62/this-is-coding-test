'''
[카드 정렬하기]
n개의 카드 묶음, 각 카드의 장 수 for in range(n)

예시)
n = 3
10, 20, 40 순으로 정렬되어 더해질 때 최소!!
우선순위 큐 활용 : 입력값이 정렬되지 않았기 때문
10 + 20 + (30) + 40 + (70) + 50 + (120) ... 
 -> 더해진 값이 다시 들어감

입력)
import heapq

n = int(input())
q = []

for _ in range(n):
    num = int(input())
    heapq.heappush(q, num)
'''

import heapq 

n = int(input())
q = []

for _ in range(n):
    num = int(input())
    heapq.heappush(q, num)

result = 0
while len(q) != 1 :
    a1 = heapq.heappop(q)
    a2 = heapq.heappop(q)
    sum = a1 + a2
    heapq.heappush(q, sum)
    result += sum

print(result)
