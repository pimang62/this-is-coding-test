'''
[연산자 끼워 넣기]
n개의 수, n-1개의 연산자(+, -, *, //)
연산자 우선순위 무시하고 앞에서부터 계산
-> 해결 : 중복순열

입력)
n = int(input())
n_list = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

if add > 0:
    add -= 1
    dfs()

채점)
https://www.acmicpc.net/problem/14888

참고) 
https://velog.io/@kimdukbae/BOJ-14888-%EC%97%B0%EC%82%B0%EC%9E%90-%EB%81%BC%EC%9B%8C%EB%84%A3%EA%B8%B0-Python

'''


# 재귀로 구현
n = int(input())
n_list = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_val = -1e9  # 최댓값 갱신
min_val = 1e9   # 최솟값 갱신

def dfs(i, answer):
    
    global max_val, min_val, add, sub, mul, div

    # 멈추는 조건 : i(index)가 n-1일 때
    if i == n-1:
        max_val = max(max_val, answer)
        min_val = min(min_val, answer)
        return max_val, min_val

    # 아직 식 정리가 끝나지 않았다면 
    else:    
        if add > 0:
            add -= 1
            dfs(i+1, answer + n_list[i+1])
            add += 1  # 다시 채워 넣기
        if sub > 0:
            sub -= 1
            dfs(i+1, answer - n_list[i+1])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, answer * n_list[i+1])
            mul += 1
        if div > 0:  # answer // n_list[i] (X) , int(answer / n_list[i]) (O)
            div -= 1
            dfs(i+1, int(answer / n_list[i+1]))
            div += 1
    
dfs(0, n_list[0])


print(max_val)
print(min_val)



# 백트래킹 구현
n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

max_val = -1e9  # 최댓값 갱신
min_val = 1e9   # 최솟값 갱신

def dfs(dep, answer, add, sub, mul, div):

    global max_val, min_val

    if dep == n:
        max_val = max(max_val, answer)
        min_val = min(min_val, answer)
        return 
    
    if add:
        dfs(dep+1, answer+num[dep], add-1, sub, mul, div)
    if sub:
        dfs(dep+1, answer-num[dep], add, sub-1, mul, div)
    if mul:
        dfs(dep+1, answer*num[dep], add, sub, mul-1, div)
    if div:
        dfs(dep+1, int(answer/num[dep]), add, sub, mul, div-1)
    
dfs(1, num[0], op[0], op[1], op[2], op[3])

print(max_val)
print(min_val)


#  중복순열로 구현 : 4ㅠ3 = 4^3
# pypy3 통과, python3 시간초과
from itertools import permutations
n = int(input())
num = list(map(int, input().split()))
op_num = list(map(int, input().split()))
operator = ['+', '-', '*', '/']
op = []

# len(2 1 1 1) : 0~3
for i in range(len(op_num)):
    # _ : 0~1 (횟수)
    for _ in range(op_num[i]):
        op.append(operator[i])

max_val = -1e9
min_val = 1e9

def solve():

    global max_val, min_val

    # case : ['+', '-', '/']
    for case in permutations(op, n-1):
        answer = num[0]
        # num[index = 1~]
        for k in range(1, n):
            # case[index = 0~]
            if case[k-1] == '+':
                answer += num[k]
            if case[k-1] == '-':
                answer -= num[k]
            if case[k-1] == '*':
                answer *= num[k]
            if case[k-1] == '/':
                answer = int(answer / num[k])
        
        max_val = max(max_val, answer)
        min_val = min(min_val, answer)
        
        '''
        if answer > max_val:
            max_val = answer
        if answer < min_val:
            min_val = answer
        '''

solve()
print(max_val)
print(min_val)


