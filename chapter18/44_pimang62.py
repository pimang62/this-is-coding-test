'''
[행성 터널]
n개의 행성, 행성을 연결하는 터널 만들기
3차원 좌표, 터널 연결 비용 min(|x_A-x_B|, |y_A-y_B|, |z_A-z_B|)
모든 행성을 터널로 연결(n-1)하는데 필요한 최소 비용?

풀이)
좌표 조합 뽑기 : combinations(2, data) -> 시간 초과
최소값 찾아 heapq -> 정렬로 풀이

입력)
n = int(input())
data = []
for _ in range(n):
    x, y, z = map(int, input().split())
    data.append((x, y, z))

채점)
https://www.acmicpc.net/problem/2887

참고)
https://velog.io/@sunkyuj/python-%EB%B0%B1%EC%A4%80-2887-%ED%96%89%EC%84%B1-%ED%84%B0%EB%84%90
'''

n = int(input())

cor =[]

for i in range(n):
    x, y, z = map(int, input().split())
    # 좌표와 행성 번호 
    cor.append((x, y, z, i))

xsort = sorted(cor, key=lambda x: x[0])
ysort = sorted(cor, key=lambda x: x[1])
zsort = sorted(cor, key=lambda x: x[2])

# 크루스칼 알고리즘
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_find(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return

# 거리 정보
def get_dist(data1, data2, typ):
    if typ == x: idx = 0
    if typ == y: idx = 1
    if typ == z: idx = 2
    # data1[3], data2[3] : 행성 두 개의 번호
    return (abs(data1[idx]-data2[idx]), data1[3], data2[3])

dist = []
for i in range(n-1):
    dist.append(get_dist(xsort[i], xsort[i+1], x))
    dist.append(get_dist(ysort[i], ysort[i+1], y))
    dist.append(get_dist(zsort[i], zsort[i+1], z))

dist.sort()

# 0-indexed
parent = [i for i in range(n)]

# 비용 지불
pay = 0
# 행성 연결
for d in dist:
    p, a, b = d
    if find_parent(parent, a) != find_parent(parent, b):
        union_find(parent, a, b)
        pay += p

print(pay)