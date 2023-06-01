'''
[퇴사]
n+1일 째 되는 날 퇴사, 남은 n일 동안 최대한 많은 상담을 하려 함
상담을 왼료하는 데 걸리는 기간 T_i와 받는 금액 P_i가 주어짐
상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익?

예시)
n = 7
     1  2  3  4  5  6  7
t =  3  5  1  1  2  4  2
p = 10 20 10 20 15 40 200
답 : 1, 4, 5일 10+20+15=45

입력)
n = int(input())

t = []
p = []

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

풀이)
점화식 : 

참고)
https://jrc-park.tistory.com/119

''' 

n = int(input())

# 1-indexed
t = []
p = []

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

# 0-indexed
d = [0 for _ in range(n+1)]

# dp 풀이
for i in range(n-1, -1, -1):  # 마지막 날 제외 거꾸로
    
    if i + t[i] <= n:
        # 다음 값을 선택하는 것과 현재 값을 선택하는 것 중 최대
        d[i] = max(d[i+1], p[i] + d[i + t[i]]) 
    else:
        # 선택하지 않았을 때 다다음 값을 결정하려면 다음 값 저장 필요
        d[i] = d[i+1]

print(d[0])


"""
# 앞에서부터 무조건 고르는게 아님!
pay_list = []

for i in range(len(t)):
    if i + t[i] >= n:
        continue
    # 첫 날 설정
    day = i
    nxt = day + t[day]
    pay = p[day]
    while nxt < n:
        if nxt + t[nxt] >= n:
            pay_list.append(pay)
            break
        pay += p[nxt]
        nxt += t[nxt]
""" 