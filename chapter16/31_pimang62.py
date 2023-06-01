'''
[금광]
n by m의 금광, 각 칸에 특정 크기의 금 들어있음
맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있음
m번에 걸쳐서 오른쪽 위(x-1, y+1), 오른쪽(x, y+1), 오른쪽 아래(x+1, y+1) 이동
채굴자가 얻을 수 있는 금의 최대 크기는?

입력)
T = int(input()) # 테스트 케이스
for t in range(T):
    n, m = map(int, input().split())
    row = list(map(int, input().split()))
    graph = []
    for i in range(0, n*m, m):
        graph.append(row[i:i+m])
    func

풀이)
 - 점화식 : d[i][j] = max(graph[i-1][j-1], graph[i][j-1], graph[i+1][j-1]) + graph[i][j]
 - 초기값 : dp[0][0] = 1 or dp[1][0] = 2 or dp[2][0] = 0 

참고)
https://techblog-history-younghunjo1.tistory.com/263
'''

import sys

input = sys.stdin.readline

def dp(graph):
    
    # 2차원 dp 리스트
    d = [[0] * (m) for _ in range(n+1)]
    for i in range(n):
        d[i][0] = graph[i][0]

    # 열 시작 지점
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                d[i][j] = max(d[i][j-1], d[i+1][j-1]) + graph[i][j]
            elif i == n-1:  # if일 때 오류!
                d[i][j] = max(d[i-1][j-1], d[i][j-1]) + graph[i][j]
            else:
                d[i][j] = max(d[i-1][j-1], d[i][j-1], d[i+1][j-1]) + graph[i][j]

    gold = 0
    for i in range(n):
        gold = max(gold, d[i][m-1])
    
    return gold
    

T = int(input()) # 테스트 케이스
for t in range(T):
    
    n, m = map(int, input().split())
    row = list(map(int, input().split()))
    
    graph = []
    for k in range(0, n*m, m):
        graph.append(row[k:k+m])
    
    print(dp(graph))
    
