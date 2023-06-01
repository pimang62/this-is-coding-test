'''
[경쟁적 전염]
n by n의 시험관, 바이러스 종류 1~k까지
매 초 번호가 낮은 종류의 바이러스부터 먼저 증식
특정 칸에 이미 어떠한 바이러스가 있다면 들어갈 수 없음
시험관 가장 왼쪽 (1, 1)
s초가 지난 후에 (x, y)에 존재하는 바이러스의 종류?

입력)
n, k

graph = []
virus = [(v, i, j)]

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[i] != 0:
            virus.append((row[i], i, j))
    graph.append(row)

풀이)
번호가 낮은 바이러스부터 앞뒤양옆으로 확산 -> 우선순위 큐?
바이러스 위치에서부터 번호가 낮은 바이러스부터 bfs
주의 : 1초일 때 비워야하는 큐, 2초일 때 비워야 하는 큐 ...
'동시'에 대해 우선 순위는 번호가 낮은 바이러스임!

채점)
https://www.acmicpc.net/problem/18405
'''
# import heapq
import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

graph = []
virus = []

time = 0
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j] != 0:
            virus.append((row[j], time, i, j))
    graph.append(row)

s, x, y = map(int, input().split())

# 정렬 후 큐 !!!
virus.sort()
q = deque(virus)

    # 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# t : time(=0) 변수로 쓰면 안 됨! 
def move(v, t, i, j, graph):
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if 0 <= ni < n and 0 <= nj < n:
            if graph[ni][nj] == 0 :
                graph[ni][nj] = v
                # 그 다음 시간에(time+1) 해야 할 일
                q.append((v, t+1, ni, nj))
    return 

while q:
    v, t, i, j = q.popleft()
    # 3초일 때 끊기
    if t == s:
        break
    move(v, t, i, j, graph)
    
print(graph[x-1][y-1])


