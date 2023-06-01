'''
[화성 탐사]
출발 지점에서 목표 지점까지 이동할 때 항상 최적의 경로를 찾도록
특정한 위치에서 인접한 곳으로 1칸씩 이동할 수 있음
n by n의 공간, [0][0]에서 [n-1][n-1]로 가는 최소 비용

입력)
T = int(input())
for _ in range(T):
    n = int(input())
    graph = []
    for _ in range(n):
        row = map(int, input().split())
        graph.append(row)

풀이)
다익스트라 알고리즘
1. 우선순위 큐 활용, 방문했는지 여부 확인 후 넣기
2. 작은 값 부터 연결하고 [n-2][n-1]나 [n-1][n-2]에 도달하면 바로 연결
3. 두 값 중 더 작은 값 출력 

예제)
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
'''
from heapq import heappop, heappush

T = int(input())
for _ in range(T):
    n = int(input())
    # 최솟값을 기록할 것이므로
    visited = [[1e9]*n for _ in range(n)]
    graph = []
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    # 움직임 정의
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    q = []
    heappush(q, (graph[0][0], (0, 0)))
        
    while q:
        c, order = heappop(q)
        x, y = order
        if visited[x][y] < c: 
            continue
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            # 조건에 맞는 방향키 중
            if 0 <= nx < n and 0 <= ny < n:
                # 이전 값과 더해진 cost
                cost = c + graph[nx][ny]
                # 최단 거리일 때 기록
                if cost < visited[nx][ny]:
                    heappush(q, (cost, (nx, ny)))
                    visited[nx][ny] = cost

    print(visited[n-1][n-1])
