'''
[실패율]

실패율  : 스테이지에 도달했으나, 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수

전체 스테이지 n개, 현재 멈춰있는 스테이지의 번호 배열 stages

예시)
n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

stages.sort() -> [1, 2, 2, 2, 3, 3, 4, 6]

fail_dict = {}

'''
# dict         테스트 22 〉	통과 (1378.09ms, 18.4MB)
# defaultdict  테스트 22 〉	통과 (1732.00ms, 18.3MB)

from collections import defaultdict

def solution(n, stages):
    fail_dict = defaultdict(float)
    stages.sort()
    num = len(stages)
    for i in range(1, n+1):
        if num != 0:
            cnt = stages.count(i)
            fail_rate = float(cnt/num)
            fail_dict[i] = fail_rate
            num -= cnt
        # 해당 stage에 도달한 사람이 없을 때
        else:
            fail_dict[i] = 0.0

    fail_dict = dict(sorted(fail_dict.items(), key=lambda x: x[1], reverse=True))
    result = [k for k in fail_dict.keys()]
    return result

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
        