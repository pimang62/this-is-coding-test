'''
[감시 피하기]
선생님(T), 학생(S), 장애물(O), Nothing(X)
선생님은 장애물 뒤편에 숨은 학생들을 볼 수 없음
 -> nx, ny 범위 밖 or O로 적힌 공간이면 안 됨
dfs로 구현하여 학생들을 모두 볼 수 있음
정확히 3개의 장애물을 설치해야 함

입력)
n = int(input())

graph = []
teacher = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j] == 'T':
            teacher.append((i, j))
    graph.append(row)

채점)
https://www.acmicpc.net/problem/18428
'''

import copy
 
n = int(input())

graph = []
teacher = []
for i in range(n):
    row = list(input().split())
    for j in range(len(row)):
        if row[j] == 'T':
            teacher.append((i, j))
    graph.append(row)


def watch(board):

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    # board 내 모든 선생님에 대하여
    for t in teacher:
        x, y = t
        # 이동 방향 설정
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 조건에 맞는 상황이면 계속 depth
            while 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 'O':
                if board[nx][ny] == 'S':
                    return False
                nx += dx[k]
                ny += dy[k]
    
    return True
    
result = "NO"
def backtracking(cnt):
    if cnt == 3:
        # 'O' 3개 채운 board 넘겨줌
        board = copy.deepcopy(graph)
        global result
        # 모든 선생님이 봤을 때 학생이 없다면
        if watch(board) == True:
            result = "YES"
        return

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                backtracking(cnt+1)
                graph[i][j] = 'X'

backtracking(0)
print(result)

'''
if result:
    print("YES")
else:
    print("NO")
'''

