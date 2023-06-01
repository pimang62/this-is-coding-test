'''
[여행 계획]
1~n까지 n개의 여행지, 양방향 이동 가능
여행 계획이 가능한지의 여부 판단?

예시)
2 -> 3 -> 4 -> 3 == 2 -> 3 -> 2 -> 4 -> 3

입력)
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

풀이)
크루스칼 알고리즘
 - find_parent, union_parant, 
 - if find_parent(parent, x) != find_parent(parent, y):
'''

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

order = list(map(int, input().split()))

parent = [k for k in range(n+1)]

def find_parent(parent, x):
    if parent[x] != x:
        # parent[x]에 적힌 parent 찾기
        parent[x] = find_parent(parent, parent[x])
    # elif parent[x] == x
    return parent[x]

def union_parent(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(parent, order):

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                # parent : 1-indexed
                union_parent(parent, i+1, j+1)

    check = "YES"
    # parent[order[0]=2]
    num = parent[order[0]]
    for o in order:
        if num != parent[o]:
            check = "NO"
            break

    return check

print(solution(parent, order))