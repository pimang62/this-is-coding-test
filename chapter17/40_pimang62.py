'''
[숨바꼭질]
1~n번까지의 헛간 중에 1번 헛간으로부터 최단 거리가 가장 먼 헛간?
 - m개의 양방향 통로 존재
 - 항상 1번 헛간에서 출발
 - 만약 거리가 같은 헛간이 여러 개면 가장 작은 헛간 번호 출력

입력)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((1, b))  # 비용 1로 둠
distance = [INF] * (n+1)

예시)
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''
from heapq import heappop, heappush

n, m = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    # 양방향 노드
    graph[a].append((1, b))
    graph[b].append((1, a))

# 최단 거리를 담을 공간
distance = [INF] * (n+1)

def dijkstra(start):

    q = []
    heappush(q, (0, start))
    distance[start] = 0

    while q:
        c, now = heappop(q)
        # distance에 이미 최단 거리 기록되어 있다면 넘어감
        if distance[now] < c:
            continue
        for val, nxt in graph[now]:  # 값, 다음 노드
            # 미리 cost 계산해 보고
            cost = c + val
            # 간선을 거치는 경우가 최단 거리라면 업데이트
            if cost < distance[nxt]:
                # 거리 확정 및 힙에 넣어주기
                distance[nxt] = cost
                heappush(q, (cost, nxt))

dijkstra(start=1)

# 가장 큰 거리를 갖는 index 중 작은 값
a = distance.index(max(distance[1:]))
# 해당 index의 거리
b = distance[a]
# 해당 거리와 같은 값을 갖는 개수
c = distance.count(b)

print(a, b, c, sep=' ')
    
