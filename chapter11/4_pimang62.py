'''
*[만들 수 없는 금액]
n개의 동전을 이용하여 만들 수 없는 양의 정수 최솟값
ex. n = 5, 3 2 1 1 9 : 1~16 수 중 최초로 만들 수 없으면 return
idea) 앞의 금액들을 모두 더해 만든 금액 + 1 이 target, 그 다음 더해야 할 금액보다 작다면 break
'''

import sys
input = sys.stdin.readline

n = int(input())

coins = list(map(int, input().split()))
coins.sort()  # 작은 순서대로

# (만들 수 있는 coin + 1)원을 만들 수 있는지 확인
target = 1
for coin in coins:
    if target < coin:
        break
    target += coin

print(target)



