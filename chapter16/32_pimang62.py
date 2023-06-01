'''
[정수 삼각형]
크기가 n인 삼각형
맨 위층부터 시작하여 아래에 있는 수 중 하나를 선택하며 내려올 때,
이제까지 선택된 수의 합이 최대가 되는 경로 !
합을 출력

입력)
n = int(input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

풀이)
 - 점화식 : d[i][j] = graph[i][j] + max(d[i-1][j-1], d[i-1][j])
 - 초기값 : d[0][0] = 7
'''

import sys
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def dp(graph):

    d = [[0]*(k+1) for k in range(n)]
    d[0][0] = graph[0][0]

    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                d[i][j] = graph[i][j] + d[i-1][j]
            elif j == i:
                d[i][j] = graph[i][j] + d[i-1][j-1]
            else:
                d[i][j] = graph[i][j] + max(d[i-1][j-1], d[i-1][j])
    
    max_val = 0
    for j in range(n):
        max_val = max(max_val, d[n-1][j])
    
    print(max_val)

dp(graph)