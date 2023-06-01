'''
[문자열 뒤집기]
0과 1로만 이루어진 문자열 S
이 문자열 S에 있는 모든 숫자를 전부 같게 !
뒤집는 최소 횟수는?
idea) 0 묶음, 1 묶음 갯수가 곧 바꾸어야 횟수
 -> 묶음을 만들어 0 or 1 중 개수 더 작은 것 return
ex. 0010101010000101111110 -> 0:7, 1:6 -> 6 !
'''

data = [int(d) for d in input()]

unit = []

num = 0
for i in range(len(data)):
    if num != data[i] :
        unit.append(data[i-1])
        num = data[i]
    
unit.append(data[-1])


d = {}
for u in unit:
    if u not in d:
        d[u] = 1
    else:
        d[u] += 1

'''
from collections import Counter
d = Counter(unit)
'''

print(min(d.values()))

    