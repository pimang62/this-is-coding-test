'''
[문자열 압축]
문자열을 1개 이상의 단위로 잘라 압축하여 더 짧은 문자열로 표현
ex. 
aaabbaccc : 3a2ba3c
'''

def zippy(s, l):
    length = l
    count = 0
    string = ''
    i = 0
    while i+length <= len(s):  # 24
        word = s[i:i+length]
        count = 1
        for j in range(i+length, len(s)+1, length):
            if word == s[j:j+length]:
                count += 1
            else:
                break
        
        if count > 1:
            string += str(count) + word
        else:
            string += word

        i = j  # 18  
        
    # 남은 문자열이 있다면 추가
    string += s[i:]  # 18~24

    return string


def solution(s):
    result = []
    # 계산 횟수를 줄이기 위해 절반까지만 : 했더니 안 됨;
    # len(s)//2 + 1도 안 됨; -> ex. len(s) -> 5 // 2 -> 2 + 1 까지는 돌아야 함!
    # cause : (len(s)//2) + 2
    for l in range(1, (len(s)//2) + 2):
        result.append(len(zippy(s, l)))
    return min(result)

print(solution('ababcdcdababcdcd'))

