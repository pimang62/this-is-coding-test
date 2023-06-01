'''
[플로이드]
n개의 도시, m개의 버스, 각 버스는 한 번 사용할 때 필요한 비용 존재
A에서 B로 가는 데 필요한 비용의 최솟값?

입력)
n = int(input())
m = int(input())

graph = [[0] * (m) for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    for i in range(n):
        for j in range(m):
            graph[a][b] = c

풀이)
플로이드 알고리즘 : 2차원 테이블 모두 갱신
graph i, j에 놓인 값들에 대해 min(graph[a][b], graph[a][k]+graph[k][b])

채점)
https://www.acmicpc.net/problem/11404
'''
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신의 경로는 0
for i in range(1, n+1):
    graph[i][i] = 0

# 같은 경로를 향한 더 작은 비용이 있을 수 있음
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

# 플로이드 알고리즘
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        # !! 가는 경로가 없을 때에도 0
        if graph[i][j] == INF:
            graph[i][j] = 0
    print(*graph[i][1:])

'''
for i in range(1, n+1):
    print(*graph[i][1:])
'''