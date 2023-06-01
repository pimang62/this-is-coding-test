'''
[병사 배치하기]
n명의 병사가 무작위로 나열, 전투력 높은 병사가 앞쪽에 오도록
특정 위치에 있는 병사를 열외시켜 남아 있는 병사 수가 최대인 것을 만족하려면?

예시)
n = 7
[1  2 3 4 5 6 7]
15 11 4 8 5 2 4
 1  2 3 3 4 5 5

답 : 15 11 8 5 4 
    -> 2

입력)
n = int(input())
general = list(map(int, input().split()))

풀이)
 - 최장 증가 부분 수열(LIS) 알고리즘
 - 점화식 : if general[i] > general[j]: d[i] = max(d[i], d[j]+1)

참고)
https://wooono.tistory.com/575

'''

n = int(input())
general = list(map(int, input().split()))

d = [0] * n
d[0] = 1

for i in range(1, n):
    for j in range(i):
        if general[j] >= general[i]:
            d[i] = max(d[i], d[j]+1)

print(n-max(d))