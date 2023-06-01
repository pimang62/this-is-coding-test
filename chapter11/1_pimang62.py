'''
[모험가 길드]
한 마을에 모험가 n명이 있습니다.
공포도가 x인 모험가는 반드시 x명 이상이어야 합니다.
최대 몇 개의 모험가 그룹을 만들 수 있는지?
 -> 공포도 1이면 1명만 데려갈 때 모임 개수 최대 !

ex. 2 3 1 2 2 -> (1) (2 2) 2 3 : 2묶음 
ex. (1) (1) (1) (2 2) (2 3 4 4) : 5묶음 
'''

n = int(input())

scare = list(map(int, input().split()))

scare.sort()

# 모집 인원 수
unit = 0

# 지원한 사람 수
count = 0

# 모임 수
result = 0

for s in scare:
    # 모집 인원 수가 더 많다면 unit update
    if unit < s:
        unit = s
    
    # 지원한 사람 세기
    count += 1
    
    # 모집 인원이 지원한 사람과 같다면 모임 결성
    if unit == count:
        result += 1
        # 초기화
        count = 0

print(result)


"""
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for s in data:  # 공포도가 낮은 것부터 차근차근
    count += 1   # 해당 그룹에 모험가 포함시키기
    if count >= s :  # 그룹에 포함된 모험가 숫자가 가장 큰 모험가의 공포도 이상이라면
        result += 1  # 그룹 카운트
        count = 0    # 모험가 수 초기화

print(result)
"""