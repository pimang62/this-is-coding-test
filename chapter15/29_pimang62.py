'''
[공유기 설치]
집 n개가 수직선 위에 있고, 집 여러 개가 같은 좌표를 갖지는 않음
집에 공유기 c개를 설치하여 가장 인접한 두 공유기 사이의 거리를 최대로!

풀이)
공유기 설치는 2개 이상이므로 -> if c == 2: distance = h[-1]-h[0]
공유기 간격(distance)을 이진 탐색 한다.
 -> 간격이 너무 커서 
 간격이 너무 작아서 공유기 설치 숫자보다 커지면 키운다.

입력)
n, c = map(int, input().split())
house = []

for _ in range(n):
    house.append(int(input()))

예시)
n, c = 5, 3
house = [1, 2, 4, 8, 9]
 -> 1, 4, 8 or 1, 4, 9

채점)
https://www.acmicpc.net/problem/2110

참고)
https://hongcoding.tistory.com/3
'''

n, c = map(int, input().split())
house = []

for _ in range(n):
    house.append(int(input()))

house.sort()

# 첫 간격은 무조건 
distance = house[-1] - house[0]


