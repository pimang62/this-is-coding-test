'''
[가사 검색]
가사에 사용된 단어들 중에 특정 키워드가 몇 개 포함되어 있는지?
ex. "fro??" : "frodo", "front", "frost"
검색 키워드는 "?"가 하나 이상 포함, 접두사 아니면 접미사!

입력)
def solution(words, queries):
    answer = []
    return answer

채점)
https://school.programmers.co.kr/learn/courses/30/lessons/60060

참조)
https://ariz1623.tistory.com/274
'''

# 효율성 1, 2, 3 >>> 시간 초과
def findidx(q):
    
    if q[0] == '?':
        i, j = 0, q.count("?")
    if q[-1]== '?':
        i, j = -(q.count("?")), -1
    return i, j

'''
    if q[0] == '?':
        i, k = 0, 1
        while q[k] == '?':
            k += 1
        j = k # 4

    if q[-1]== '?':
        k, j = -2, -1
        while q[k] == '?':
            k -= 1
        i = k+1 # -3+1
    return i, j
'''

'''
    i, j = len(q), 0
    for k in range(len(q)):
        if q[k] == '?':
            i, j = min(i, k), max(j, k)
    return i, j
'''

def coincidence(words, q):
    cnt = 0
    # "?"의 인덱스 찾아오기
    i, j = findidx(q)
    for w in words:
        if len(w) != len(q):
            continue
        # "?"가 접두사에 있다면 & 뒷 줄 같은지 보기
        if i == 0 and q[j:] == w[j:]:
            cnt += 1
        # "?"가 접미사에 있다면 & 앞 줄 같은지 보기
        if j == -1 and q[:i] == w[:i]:
            cnt += 1            
    return cnt

def solution(words, queries):
    answer = []
    for q in queries:
        answer.append(coincidence(words, q))
    return answer

print(solution(words=["frodo", "front", "frost", "frozen", "frame", "kakao"], queries=["fro??", "????o", "fr???", "fro???", "pro?"]))


# dict 형태로 저장 후 이진 탐색
from collections import defaultdict
from bisect import bisect_left, bisect_right

def makedict(words):
    words_dict, words_reverse = defaultdict(list), defaultdict(list)
    for w in words:
        words_dict[len(w)].append(w)
        words_reverse[len(w)].append(w[::-1])    
    # dict 내부 정렬
    for key in words_dict:
        words_dict[key] = sorted(words_dict[key])
        words_reverse[key] = sorted(words_reverse[key])

    return words_dict, words_reverse


def findidx(words_list, l, r):
    if not words_list:    
        lidx, ridx = 0, 0  # 필요 없음
    lidx = bisect_left(words_list, l)
    ridx = bisect_right(words_list, r)
    return lidx, ridx


def solution(words, queries):
    result = []
    
    words_dict, words_reverse = makedict(words)
    for q in queries:
        # '?'가 접미사라면 word_dict에서 찾기
        if q[0] != '?':
            l, r = q.replace('?', 'a'), q.replace('?', 'z')
            lidx, ridx = findidx(words_dict[len(q)], l, r)
        # '?'가 접두사라면 words_reverse에서 찾기
        else:
            l, r = q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z')
            lidx, ridx = findidx(words_reverse[len(q)], l, r)
        
        result.append(ridx-lidx)
    
    return result

print(makedict(words=["frodo", "front", "frost", "frozen", "frame", "kakao"]))
print(solution(words=["frodo", "front", "frost", "frozen", "frame", "kakao"], queries=["fro??", "????o", "fr???", "fro???", "pro?"]))
