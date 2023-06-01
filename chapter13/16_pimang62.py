'''
[연구소]
크기가 n by m인 공간, 0은 빈칸, 1은 벽, 2는 바이러스
아무런 벽을 세우지 않는다면 바이러스는 모든 빈칸으로 퍼질 수 있음
새로 세울 수 있는 벽은 3개이며, 꼭 3개를 세워야 함 -> 완전 탐색?
벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 안전 영역의 크기?

입력)
n, m

graph = []
virus = []

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):  # len(row)
        if row[j] == 2:
            # virus 위치 기록
            virus.append((i, j))
    # 전체 그래프 기록
    graph.append(row)

풀이)
벽 3개를 채우는 경우의 수가 담긴 그래프
해당 그래프를 복사하여 bfs 수행시킴
복사한 그래프의 0의 갯수 count 

채점)
https://www.acmicpc.net/problem/14502
: python3 시간 초과, PyPy로 통과
'''
import sys
from collections import deque
import copy

input = sys.stdin.readline
n, m = map(int, input().split())

graph = []
virus = []

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):  # len(row)
        if row[j] == 2:
            # virus 위치 기록
            virus.append((i, j))
    # 전체 그래프 기록
    graph.append(row)

    # 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = 0
def bfs(data):
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] == 0:
                    data[nx][ny] = 2
                    q.append((nx, ny))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                cnt += 1
    
    global result
    result = max(result, cnt)
    return
    
def solution(count):
    if count == 3:
        data = copy.deepcopy(graph)
        bfs(data)
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                solution(count)
                graph[i][j] = 0
                # ?
                count -= 1 

solution(0)
print(result)