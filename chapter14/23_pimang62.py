'''
[국영수]
n명의 이름, 국어, 영어, 수학

조건)
1. 국어 내림차순 reverse
2. 국어가 같으면, 영어 오름차순
3. 국어와 영어가 같으면, 수학 내림차순 reverse
4. 모든 점수가 같으면 이름 사전 순 오름차순

입력)
n = int(input())

data = []
for _ in range(n):
    data.append((name, rnr, dud, tnt))

sorted(data, key=lambda x: x[1])
sorted(data, key=lambda x: x[2], reverse=True)
sorted(data, key=lambda x: x[3])

채점)
https://www.acmicpc.net/problem/10825
'''

n = int(input())

data = []
for _ in range(n):
    data.append(input().split())

# 튜플 형태로 조건 추가 가능
data.sort(key=lambda x: (-int(x[1]), int(x[2]), (-int(x[3])), x[0]))

for d in data:
    print(d[0])