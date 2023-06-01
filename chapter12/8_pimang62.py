'''
[문자열 재정렬]
'알파벳 오름차순 정렬 + 모든 숫자 sum'
'''

string = input()

alpha = []
n = []

for s in string:
    if s.isdigit() == True:
        n.append(int(s))
    else :
        alpha.append(s)

alpha.sort()
alphabet = "".join(alpha)
summary = str(sum(n))

print(alphabet + summary)