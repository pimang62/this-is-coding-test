'''
[정렬된 배열에서 특정 수의 개수 구하기]
n개의 원소를 포함하고 있는 수열 오름차순으로 정렬
이때 이 수열에서 x가 등장하는 횟수 계산?

입력)
n, x = map(int, input().split())
num = list(map(int, input().split()))
'''

n, x = map(int, input().split())
num = list(map(int, input().split()))

# 재귀로 구현
start, end = 0, len(num)
mid = (start + end) // 2

def binary(num, start, end):
    
    global mid

    if x < num[0] or x > num[-1]:
        return -1

    while num[mid] != x:
        mid = (start + end) // 2

        if num[mid] > x:
            end = mid
            num = num[:end]
            binary(num, start, end)

        if num[mid] < x:
            start = mid
            num = num[start:]
            binary(num, start, end)

    if num[mid] == x:
            return num.count(x)
    
print(binary(num, start, end))


# bisect 라이브러리 활용
from bisect import bisect_left, bisect_right

st, en = bisect_left(num, x), bisect_right(num, x)
if (en-st) == 0:
    print(-1)
else:
    print(en-st)
     