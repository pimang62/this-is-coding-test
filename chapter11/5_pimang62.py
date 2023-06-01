'''
[볼링공 고르기]
두 사람이 서로 무게가 다른 볼링공을 고르려고 합니다.
볼링공은 총 1~n번까지 적혀있으며, 무게는 1~m까지 존재합니다.
두 사람이 공을 고르는 경우의 수는?
ex. n = 5, m = 3 
 -> 1 3 2 3 2 : (3, 3), (2, 2) 제외 총 10가지 중 8가지
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

bowl = list(map(int, input().split()))

# 경우의 수 count
count = 0
for i in range(len(bowl)):
    for j in range(i+1, len(bowl)):
        # 선택된 두 값이 같으면 넘어감
        if bowl[i] == bowl[j]:
            continue
        else:
            count += 1

print(count)


""" *
n, m = map(int, input().split())

data = list(map(int, input().split()))

array = [0] * 11  # 1 ~ 10까지의 무게 리스트

for x in data:  # 공 개수 기록
    array[x] += 1

# idea) A가 선택한 공을 제외하고 B가 선택
result = 0

for i in range(1, m+1):
    n -= array[i]  # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n  # B가 선택하는 경우의 수와 곱하기

print(result)
"""