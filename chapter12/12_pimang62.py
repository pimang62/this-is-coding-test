'''
[기둥과 보 설치]
2차원 벽면은 n by n 크기

규칙)
 - 기둥은 바닥(0) 위 or 또 다른 기둥(0) 위 or 보(1)의 왼쪽 위 or 보(1)의 오른쪽[기준] 위
    if y == 0 or [x, y-1, 0] in graph or 
    [x-1, y, 1] in graph or [x, y, 1] in graph
 - 보는 왼쪽[기준] 끝 부분이 기둥(0) 위 or 오른쪽 끝 부분이 기둥(0) 위 or (왼쪽 끝 부분이 다른 보(1) and 오른쪽 끝 부분이 다른 보(1))
    if [x, y-1, 0] in graph or [x+1, y-1, 0] in graph or 
    ([x-1, y, 1] in graph and [x+1, y, 1] in graph)

'''
from bisect import insort
def solution(n, build_frame):
    
    graph = []
    for _ in range(n):
        graph.append([-1] * (n+1))
    
    # 바닥 정보만 다르게
    graph.append([0] * (n+1))
    return graph

