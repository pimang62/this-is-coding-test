'''
[탑승구]
1~g까지의 g개의 탑승구
공항에는 p개의 비행기 도착 예정
* i번째 비행기를 1부터 g_i번째 탑승구 중 하나에 도킹
이때, 다른 비행기가 도킹하지 않은 탑승구에만 도킹

만약, 어떠한 탑승구에도 도킹할 수 없을 때에는 운행 중지
최대한 많은 비행기 도킹, 최대 몇 개?

입력)
g = int(input())
p = int(input())
data = []
for _ in range(p):
    data.append(int(input()))

풀이)
최소 신장 트리
0~g까지의 gate table 0 1 2 3 ... g
plane 값의 바로 앞과 같은 노드로 연결
...

참고)
크루스칼 : https://velog.io/@thguss/%EC%BD%94%ED%85%8C-%EC%8A%A4%ED%84%B0%EB%94%94-%EA%B7%B8%EB%9E%98%ED%94%84-%EC%9D%B4%EB%A1%A0-%ED%83%91%EC%8A%B9%EA%B5%AC
이진 탐색 : https://codlingual.tistory.com/m/213
'''

g = int(input())
p = int(input())

parent = [i for i in range(g+1)]

def find_parent(parent, x):
    if parent[x] == x:
        return parent[x]
    # parent[x]: 자식 항에서 부모 항으로 업데이트
    parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return

cnt = 0
for _ in range(p):
    plane = int(input())
    if find_parent(parent, plane) == 0:
        break
    elif find_parent(parent, plane) != find_parent(parent, plane-1):
        union_parent(parent, plane, plane-1)
        cnt += 1

print(cnt)



''' 순서를 고려해야 하므로 실패
data = []
for _ in range(p):
    data.append(int(input()))
# 내림차순 : 4 1 1
data.sort(reverse=True)

# 0 1 2 3 4
gate = [0] * (g+1)

def greedy(gate, data):
    # 최대한 많은 plane
    for d in data:
        # 뒤에서부터 채움
        for i in range(d, 0, -1):
            # 뒤에서부터 0인 곳에 docking
            if gate[i] == 0:
                gate[i] = 1
                break

    # 도킹된 plane 숫자
    return gate.count(1)

print(greedy(gate, data))
    
'''








