'''
특정 거리의 도시 찾기
최단 거리가 K인 모든 도시들의 번호 출력

메모리 초과 원인: while 문에서 거리가 K일때 break하지 않으면 발생
참고: 2. dijsktra 알고리즘
'''

from collections import deque
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

# 1. BFS
# def BFS():
#     answer = [] # X로부터 최단거리가 K인 도시 번호 저장
#
#     queue = deque([(0,X)]) # (weight, start)
#     visited[X] = True  # 방문표시
#     while queue:
#         dist, v = queue.popleft()
#         if dist == K:  break # 이후부터는 최단거리가 K이상이므로 종료
#
#         for u in graph[v]:
#             if not visited[u]:
#                 visited[u]=True # 방문표시
#                 queue.append((dist+1, u))
#                 if dist+1==K: # 최단 거리가 K
#                     answer.append(u)
#     return sorted(answer)
#
# N, M, K, X = map(int, input().split()) # 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
# graph = [[] for _ in range(N+1)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     graph[a].append(b)
# visited = [False]*(N+1)
#
# answer = BFS()
# if answer: print(*answer,sep='\n')
# else: print(-1) # 빈 리스트



# ***********************************************************************************
# 2. Dijsktra
INF = int(1e9)
def Dijsktra():
    d = [INF] * (N + 1)  # 최단 거리
    pq = []
    d[X] = 0
    heappush(pq,(0,X))
    while pq:
        w,v = heappop(pq)
        if w==K: break # heap은 가중치가 작은 순으로 정렬되기 때문에 미리 종료 가능
        if d[v]<w: continue
        for u in graph[v]: # 가중치는 모두 1
            if d[u] > d[v]+1:
                d[u] = d[v]+1
                heappush(pq, (d[u],u))
    return d


N, M, K, X = map(int, input().split()) # 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

d = Dijsktra()
flag = False # 최단 거리 K 존재여부
for i in range(1,N+1):
    if d[i]==K:
        print(i)
        flag = True
if not flag: print(-1)
