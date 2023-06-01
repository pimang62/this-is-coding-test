'''
[안테나]
n개의 집, 집 위치 정보 기록
안테나로부터 모든 집까지의 거리의 총합이 최소가 되도록!

입력)
n = int(input())
data = list(map(int, input().split()))

distance = [1e9] * (n+1)

채점)
https://www.acmicpc.net/problem/18310
'''
# 시간 초과
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

distance = [1e9] * (max(data)+1)

# 중간값의 왼쪽 중간부터 오른쪽 중간까지 
i = max(data)//4
while i <= 3*(max(data)//4):
    dist = 0
    for d in data:
        dist += abs(d-i)
    distance[i] = dist
    i += 1

idx = distance.index(min(distance))

print(idx)

# 중간값 : 홀수) n+1/2, 짝수) n/2, n+1/2의 평균 
n = int(input())
data = list(map(int, input().split()))
data.sort()
print(data[(n-1)//2]) # 중간값 중 최소 

