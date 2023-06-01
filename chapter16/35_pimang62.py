'''
[못생긴 수]
못생긴 수란 오직 2, 3, 5만을 소인수로 가지는 수
1은 못생긴 수, {1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15 ...}
n번째 못생긴 수는?

입력)
n = int(input())

풀이)
 - 점화식 : d[i] = min(num2, num3, num5)
 - 매 순간 현재의 값이 최소가 되게끔
 
참고)
https://velog.io/@juyeonma9/%EC%9D%B4%EC%BD%94%ED%85%8C-%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EB%AA%BB%EC%83%9D%EA%B8%B4%EC%88%98-python
'''

n = int(input())

# 0-indexed
d = [0 for _ in range(n+1)]
d[1] = 1

# 첫 세 가지 숫자들을 제외하면 그 이상은 불필요
i2 = i3 = i5 = 1

num2, num3, num5 = 2, 3, 5

# d[n] 테이블까지 채울 것
for i in range(2, n+1):

    d[i] = min(num2, num3, num5)

    if d[i] == num2:
        # 2가 있는 자리 지정
        i2 += 1
        num2 = d[i2] * 2
    
    if d[i] == num3:
        # 3이 있는 자리 지정
        i3 += 1
        num3 = d[i3] * 3

    if d[i] == num5 :
        i5 += 1
        num5 = d[i5] * 5

print(d[n])
