'''
[어두운 길]
n개의 집과 m개의 도로, 각 집은 0~n-1번까지로 구분
특정한 도로의 가로등을 하루 동안 켜기 위한 비용은 길이와 동일
일부 가로등을 비활성화하여 최대한 많은 금액이 되도록?
 -> 최소 신장 트리

입력)
n, m = map(int, input().split())
data = []
for _ in range(m):
    a, b, c = map(int, input().split())
    data.append((-c, a, b))
cost = [0] * n

예시)
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
'''

from heapq import heapify, heappop

n, m = map(int, input().split())

data = []
value = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    data.append((c, a, b))
    value += c

cost = 0
parent = [i for i in range(n)]

# 실험
rest = 0

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_find(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    check = True
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b
    else:
        check = False
    return check

heapify(data)  # q = heapify(data) : X
while data:
    c, a, b = heappop(data)
    if union_find(parent, a, b):
        cost += c
    elif union_find(parent, a, b) == False:
        rest += c

print(value - cost)

# 실험
print(rest)




