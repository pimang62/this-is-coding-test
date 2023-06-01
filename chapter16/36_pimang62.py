'''
[편집 거리]
두 개의 문자열 A와 B, A를 편집하여 B로 만들고자 함
1. 삽입 : 특정한 위치에 하나의 문자를 삽입함
2. 삭제 : 특정한 위치에 있는 하나의 문자를 삭제
3. 교체 : 특정한 위치에 있는 하나의 문자를 다른 문자로 교체

입력)
A = map(input().split())
B = map(input().split())

예시)
sunday
saturday
>>> 3

cat
cut
>>> 1

풀이)
 - 문자열 유사도 측정 알고리즘
 - 2차원 메모제이션 배열을 사용하는 DP
 - 점화식 : d[i][j] = min(d[i-1][j-1], d[i][j-1], d[i-1][j])

참고)
https://joyjangs.tistory.com/38
'''

A = input()
B = input()

d = [ [0] * (len(A)+1) for _ in range(len(B)+1) ]

# 한 글자 채우는 건 +1만 하면 되므로
for i in range(1, len(A)+1):
    d[0][i] = i
for j in range(1, len(B)+1):
    d[j][0] = j

# dp 수행
for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        
        # 같은 문자가 같은 위치에 있을 땐 굳이 수정 안 함
        if A[i-1] == B[i-1]:
            d[i][j] = d[i-1][i-1]

        else:
            d[i][j] = min(d[i-1][j-1], d[i-1][j], d[i][j-1]) + 1

print(d[-1][-1])