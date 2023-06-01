'''
*[인구 이동]
n by n 크기의 땅, 인접한 나라 사이 국경선 존재함
두 나라의 인구 차이가 L명 이상 R명 이하라면 연합국
각 칸의 인구 수 = (연합 인구 수) / (연합 이루고 있는 칸의 개수)
인구 이동이 몇 번 발생하는지?

입력)
n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

풀이)
현재 칸의 숫자와 다음 칸의 숫자 차이가 l이상 r이하라면 연합국 q 추가
q를 빼면서 연합국들 간의 평균값으로 그래프 변경
반복..

채점)
https://www.acmicpc.net/problem/16234
'''
from collections import deque

n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


def bfs(x, y):

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 연합국 넣기
    union = [(x, y)]
    value = graph[x][y]

    # 탐색 초기값
    q = deque([(x, y)])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] == 1:
                continue
            if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                union.append((nx, ny))
                value += graph[nx][ny]
                # 조건에 맞는 애들만 방문 처리 !!
                visited[nx][ny] = 1
                # 조건에 맞는 애들만 q에 넣어주기
                q.append((nx, ny))
    
    for uni in union:
        i, j = uni
        graph[i][j] = value // len(union)
    
    return union

cnt = 0
while True:
    flag = False
    # 방문 여부 : 한 그래프 내에서 union을 찾고, 
    # 매 횟수마다 새로 갱신해야 하기 때문 !!
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] != 1:
                # 연합국이 2개 이상일 때
                if len(bfs(i, j)) > 1:
                    flag = True
            
    if not flag:
        break
    cnt += 1
    
print(cnt)
