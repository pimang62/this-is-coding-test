'''
[고정점 찾기]
고정점(fixed point)이란, 수열의 원소 중에서 그 값이 인덱스와 동일한 원소
ex. a = [-15, -4, 2, 8, 13] -> a[2] = 2 고정점!
고정점은 최대 1개, 만약 고정점이 없다면 -1 출력

입력)
n = int(input())
num = list(map(int, input().split()))
'''

n = int(input())
num = list(map(int, input().split()))
visited = [False] * n

start, end = 0, len(num)
mid = (start + end) // 2

while mid != num[mid]:
    
    # 계속된 반복 구간이 생길 때 -1
    if visited[mid] == True:
        break
    
    # idx가 값보다 크면 오른쪽으로
    if mid > num[mid]:
        start = mid
        visited[mid] = True
    
    # idx가 값보다 작으면 왼쪽으로
    if mid < num[mid]:
        end = mid
        visited[mid] = True

    mid = (start + end) // 2

# 고정점이 있으니 -1 
if mid == num[mid]:
    print(mid)

# 고정점이 없으니 -1 
if visited[mid] == True:
    print(-1)