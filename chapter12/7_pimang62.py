'''
[럭키 스트레이트]
점수 n이 주어지면, 반으로 나누어 왼쪽과 오른쪽의 합이 같은지 아닌지 ?
'''

n = [int(i) for i in input()]
half = int(len(n)/2)

left = n[:half]
right = n[half:]

if sum(left) == sum(right):
    print("LUCKY")

else:
    print("READY")