'''
[정확한 순위]
n명의 성적, m번의 비교
성적 순위를 정확히 알 수 있는 학생은 모두 몇 명?

입력)
n, m = map(int, input().split())

data = [ [1e9] * (n+1) for _ in range(n+1) ]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 0

풀이)
 - 성적이 낮은 학생이 나에게로 도달 가능하고, 내가 성적이 높은 학생에게 도달 가능하다면
 - 순위를 알 수 있음!
 - 양쪽을 확인 하였을 때 하나라도 도달 불가하면, 내 순위를 알 수 없음 !
 - if graph[a][b] == graph[b][a] == INF:

참고)
https://velog.io/@juyeonma9/%EC%9D%B4%EC%BD%94%ED%85%8C-%EC%B5%9C%EB%8B%A8%EA%B2%BD%EB%A1%9C-%EC%A0%95%ED%99%95%ED%95%9C%EC%88%9C%EC%9C%84-python
 '''

import sys
input = sys.stdin.readline
# sys.maxsize : int형의 최대값 (2^31-1)
INF = int(1e9)

n, m = map(int, input().split())
data = [ [INF] * (n+1) for _ in range(n+1) ]

# 자기 자신의 성적 아는 것은 0
for i in range(n):
    data[i][i] = 0

# 확인된 성적 기록
for _ in range(m):
    a, b = map(int, input().split())
    data[a][b] = 0

# data[i][j]를 알거나 data[i][k]+data[k][j]를 알 때는 성적 확인 가능
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            data[i][j] = min(data[i][j], data[i][k]+data[k][j])

cnt = 0
for i in range(1, n+1):
    check = True
    for j in range(1, n+1):
        # 양쪽을 확인 하였을 때 하나라도 모르면, 내 순위를 알 수 없음 !
        if data[i][j] == data[j][i] == INF:
            check = False
    if check == True:
        cnt += 1   
print(cnt)


