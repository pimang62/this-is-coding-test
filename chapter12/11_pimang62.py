'''
[뱀]
n by n 정사각 보드 위, 뱀은 (1, 1)에 위치합니다.
1. 뱀은 몸 길이를 늘려 머리를 다음 칸에 위치시킵니다. (x+dx, y+dy)
2. 만약 이동한 칸에 사과가 있다면(1), 꼬리는 움직이지 않습니다.
3. 만약 이동한 칸에 사과가 없다면(0), 꼬리가 위치한 칸을 비워줍니다. (x, y) = 0
이 게임은 몇 초에 끝나는지? (count)

제어문) 
뱀이 이리저리 기어다니다가 벽(nx, ny<0 or nx, ny>n) 또는 자기 자신의 몸(1)과 부딪히면 게임이 끝남!
if nx<0 or ny<0 or nx>=n or ny>=n : 
    break -> count 출력
if graph[nx][ny] > 0 :
    break -> count 출력

자료구조) 
뱀이 오른쪽으로 이동 (동)
dx = x + 0, dy = y + 1
if direction == 'D': (남)
dx = x + 1, dy = y + 0
if 'L' : (동)
elif 'D' : (서)
...
 -1 L 동 남 서 북 D +1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

2D 그래프)
사과 있는 위치 -1 기록, 뱀 처음 위치 [0][0] = 1
뱀이 머물렀던 자리 리스트, 뱀 길이 length
direction time동안 뱀 이동시키기 -> 제어문) 통과 
-> 사과가 없으면 (graph[nx][ny] == 0) -> 1 -> 뱀이 지나간 자리(nx, ny) 리스트 추가 
-> def 뱀[:-length] = 0으로 만들어주기 -> x, y = nx, ny 
 
-> 사과가 있으면 (graph[nx][ny] == -1) -> 1 -> 뱀이 지나간 자리(nx, ny) 리스트 추가 
-> length += 1 -> x, y = nx, ny -> def 뱀[:-length] = 0으로 만들어주기 
...
'''

n = int(input())    # 6
k = int(input())    # 3

graph = [[0]*n for _ in range(n)]   # 0~5, 0~5 

# 사과 위치 업데이트
for _ in range(k):
    a, b = map(int, input().split())
    # index 0부터 시작
    graph[a-1][b-1] = -1

# 방향 위치 변환 횟수
l = int(input())

direction = []  # 3 D, 15 L
for _ in range(l):
    time, direc = input().split()
    direction.append([int(time), direc])

#  L 동  남 서  북 D 
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 뱀이 지나간 자리
snake = []

# 초기값 설정
x, y = 0, 0
graph[x][y] = 1
snake.append((x, y))

# 꼬리 자르기 함수
def makeitzero(snake):
    tx, ty = snake.pop(0)
    graph[tx][ty] = 0
    return graph

# 초기값 설정
count = 0
length = 1

# direction index
i = 0
# direction pointer
j = 0

'''
# 방향 전환 함수
def turn(direction, c):
    if c == 'D':
        return (i + 1) % 4
    else:
        return (i - 1) % 4  
'''
            
# time이 끝나도 뱀은 움직여야 하니까 while문  
while True:
            
    nx = x + dx[i]
    ny = y + dy[i]

    # 범위를 벗어나면
    if nx<0 or ny<0 or nx>=n or ny>=n : 
        count += 1
        break
            
    # 뱀 길이에 닿는다면
    if graph[nx][ny] > 0 :
        count += 1
        break
        
    # 사과가 없다면
    if graph[nx][ny] == 0:  
        graph[nx][ny] = 1
        # 머리 추가
        snake.append((nx, ny))
        # 꼬리 제거
        makeitzero(snake)
                
    # 사과가 있다면
    if graph[nx][ny] == -1:
        graph[nx][ny] = 1
        # 머리 추가
        snake.append((nx, ny))
            
    x, y = nx, ny
    count += 1

    # 방향 바꿀 시간이 되면
    if count == direction[j][0] :
        
        # 갈 수 있으면 direction 바꾸기
        if direction[j][1] == "D":
            i = (i + 1) % 4
        else:
            i = (i - 1) % 4
        
        # direction pointer 변경(if j == 4)
        j = (j + 1) % len(direction) 
    
    else:
        continue

'''
    # pointer < len(direction) & 방향 바꿀 시간이 되면 
    if j < l and count == direction[j][0] :
        
        i = turn(direction, direction[j][1])
        j += 1
'''

print(count)
