'''
[특정 거리의 도시 찾기]
1~n번까지의 도시, m개의 단방향 도로, 최단 거리가 k인, x에서 출발
최단 거리가 k인 모든 도시의 번호를 한 줄에 하나씩 오름차순
이때, 최단 거리가 k인 도시가 하나도 존재하지 않으면 -1

입력)
n, m, k, x

graph = [ [] for _ in range(n+1) ]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

풀이)
최단거리 문제 : bfs

채점)
https://www.acmicpc.net/problem/18352
'''

import sys
input = sys.stdin.readline

from collections import deque

n, m, k, x = map(int, input().split())

graph = [ [] for _ in range(n+1) ]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# [0]이면 양방향 노드 시 자기 자신 0으로 리셋 안됨
distance = [-1] * (n+1)     # 일반적으로 -1
distance[x] = 0

q = deque([x])
# q.append(x)   # 런타임 에러 범인
while q:
    now = q.popleft()   # 1
    for nxt in graph[now]:   # 2, 3
        if distance[nxt] == -1:
            distance[nxt] = distance[now] + 1
            q.append(nxt)

for i in range(len(distance)):
    if distance[i] == k:
        print(i)

if k not in distance:
    print('-1')

'''
check = False
for i in range(len(distance)):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
'''



