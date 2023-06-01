'''
[곱하기 혹은 더하기]
각 자리가 숫자(0부터 9)로만 이루어진 '문자열' S 
 -> int(s) 필요
+ 혹은 * 연산을 했을 때 가장 큰 수 가 만들어져야 함 
 -> DP 이용
'''

# 문자열
S = input()

# int로 바꾸어 리스트화
s = [int(s) for s in S]

# * 연산과 + 연산 중 더 큰 값 update
for i in range(1, len(S)):
    s[i] = max(s[i-1] + s[i], s[i-1] * s[i])

print(s[-1])


""" 
data = input()

result = int(data[0])  # 첫 번째 숫자(0 아님!)

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:  # 둘 중 하나라도 1 이하면 +
        result += num
    else:  # 둘 중 하나라도 1 초과(2 이상)면 *
        result *= num

print(result)
"""