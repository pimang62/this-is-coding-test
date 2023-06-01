'''
[괄호 변환]
'('와 ')'로만 이루어진 문자열 w가 "균형잡힌 괄호 문자열"이라면,
1. 입력이 빈 문자열 -> 빈 문자열 반환
2. 문자열 w를 두 "균형잡힌 문자열" u, v로 분리
    -> "균형잡힌 문자열"인지 확인하는 함수 필요 
3. 수행한 결과 문자열을 u에 이어 붙인 후 반환 (+=)
 3-1. 문자열 u가 "올바른 괄호 문자열이라면, 
    문자열 v에 대해 1단계부터 다시 수행 (재귀)
 3-2. 문자열 u가 "올바른 괄호 문자열이 아니라면,
    1) 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 반환
        -> 이어 붙임
    2) 빈 문자열에 첫 번째 문자로 '('를 붙임 
        -> 빈 문자열일 수 있으니
    3) ')'를 다시 붙임
    4) 앞 뒤 '('과 ')'를 제거하고 나머지 괄호 방향을 뒤집어 붙이기

채점)
https://www.programmers.co.kr/learn/courses/30/lessons/60058
 ''' 

def balanced_idx(s):
    count = 0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        else:  # ')'
            count -= 1
        if count == 0:
            break
    return i+1  # u, v = w[:i+1], w[i+1:]

def right(s):
    count = 0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        else:  # ')'
            count -= 1
        if count < 0:  # -가 되는 순간이 한 순간이라도 존재할 시 ')'부터 시작한 것
            return False
    return True

def solution(w):
    result = ''
    if w == '':
        return result
    u, v = w[:balanced_idx(w)], w[balanced_idx(w):]
    
    if right(u) == True:
        result = u+solution(v)
    else:
        result += '(' + solution(v) + ')'
        for i in u[1:-1]:
            result += '(' if i == ')' else ')'
    return result

