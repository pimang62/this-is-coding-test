'''
*[자물쇠와 열쇠]
열쇠 행렬 m by m, 자물쇠 행렬 n by n

행렬 90도 회전 : array[x]][y] = array[y][N-1-x]
행렬 180도 회전 : array[x]][y] = array[N-1-y][N-1-x]
행렬 270도 회전 : array[x]][y] = array[N-1-y][x]
행렬 360도 회전 : array[x]][y] = array[x][y]

그래프)
graph = [[0]*m*m for _ in range(n*n)]   # 그래프 배로 증량
graph[i+n][j+n] = lock[i][j]            # 중앙에 자물쇠 넣기
graph[x+i][y+j] = key[i][j]             # x, y 증가하며 키 넣기

*참고 : https://velog.io/@tjdud0123/%EC%9E%90%EB%AC%BC%EC%87%A0%EC%99%80-%EC%97%B4%EC%87%A0-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B3%B5%EC%B1%84-python

함수)
def rotation():
행렬 90도 회전 : array[x]][y] = array[y][N-1-x]

def check():
열쇠의 돌기 1 부분과 자물쇠의 홈 0 부분이 정확히 일치하도록
-> 두 행렬을 더한 값이 모두 1이면 True !

def key_push():
    for x in range((n*3)-m):
        for y in range((n*3)-m):
            graph[x+i][y+j] += key[i][j]

def key_pull():
    for x in range((n*3)-m):
        for y in range((n*3)-m):
            graph[x+i][y+j] -= key[i][j]

'''

# 행렬 회전 함수 
def rotation(array):
    
    # 4 by 2
    n = len(array)      # 행 ex. 4
    m = len(array[0])   # 열 ex. 2
    # 행과 열을 바꾸어 선언
    result = [[0]*n for _ in range(m)]  # 2 by 4
    
    # 행 정보
    for x in range(n):
        # 열 정보
        for y in range(m):
            result[y][n-1-x] = array[x][y]
    
    return result


# 모두 1인지 체크하는 함수
def check(graph):
    length = len(graph) // 3    # 9 // 3 = 3 
    for i in range(length, length*2): # 3 ~ 6
        for j in range(length, length*2):     
            # 만약 하나라도 1이 아니라면 !
            if graph[i][j] != 1:
                return False
    # 기본값
    return True


# 키 넣기 함수
def key_push(x, y, m, graph, key):
    for i in range(m):
        for j in range(m):
            graph[x+i][y+j] += key[i][j]


# 키 빼기 함수
def key_pull(x, y, m, graph, key):
    for i in range(m):
        for j in range(m):
            graph[x+i][y+j] -= key[i][j]


def solution(key, lock):

    n, m = len(lock), len(key)
    
    # 그래프 3배로 증량 : len(lock)*3만큼만 그래프 늘리면 됨 !
    graph = [[0]*n*3 for _ in range(n*3)]
    
    # lock 행렬에 대하여
    for i in range(n):
        for j in range(n):     

            # 중앙에 자물쇠 끼워넣기
            graph[i+n][j+n] = lock[i][j]    # [3][3]


    # key 돌려보아야 하므로 넓은 범위의 반복 !
    for _ in range(4):

        key = rotation(key)

        # 그래프 행렬에 대하여, (n*3)-m : key 넣을 마지막 공간까지
        for x in range(len(graph)-m):
            for y in range(len(graph)-m):
                
                key_push(x, y, m, graph, key)

                # 합이 1인지 check 함수 필요
                if check(graph) == True:
                    return True
                    
                # *넣은 키 다시 빼기(-) : i, j 반복문이 끝났으므로 다시 선언
                key_pull(x, y, m, graph, key)

    # 기본 값
    return False
    

print(solution(key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]],
               lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))


''' 
*참고 by 교재

def solution(key, lock):

    n = len(lock)
    m = len(key)
    
    # 그래프 3배로 증량 : len(lock)*3만큼만 그래프 늘리면 됨 !
    graph = [[0]*n*3 for _ in range(n*3)]
    
    # lock 행렬에 대하여 : 자물쇠 행렬은 없어지면 안되므로 미리 선언
    for i in range(n):
        for j in range(n):     

            # 중앙에 자물쇠 끼워넣기
            graph[i+n][j+n] = lock[i][j]    # [3][3]


    # key 돌려보아야 하므로 넓은 범위의 반복 !
    for _ in range(4):  # 90 ~ 360까지

        key = rotation(key)

        # 그래프 행렬에 대하여 : len(graph) 범위까지 가면 x+i 범위 벗어날수도
        for x in range(n*2):
            for y in range(n*2):
                
            # key 행렬에 대하여
                for i in range(m):
                    for j in range(m):
                        
                        # 키 채워 넣기(+)
                        graph[x+i][y+j] += key[i][j]     # [0][0] -> [0][1] ...

                # 합이 1인지 check 함수 필요
                if check(graph) == True:
                    return True
                    
                # *넣은 키 다시 빼기(-) : i, j 반복문이 끝났으므로 다시 선언
                for i in range(m):
                    for j in range(m):
                        graph[x+i][y+j] -= key[i][j]

    # 기본 값
    return False
'''