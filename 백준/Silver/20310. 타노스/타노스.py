import sys

# 문자열 읽기
S = list(sys.stdin.readline().rstrip())

# '0'과 '1'의 개수 계산
N = S.count('0')
M = S.count('1')

# '1'을 제거해야 할 개수
remove1 = M // 2

# '0'을 제거해야 할 개수
remove0 = N // 2

result = []

# '1' 제거 (앞에서부터 절반)
count1_removed = 0
for char in S:
    if char == '1' and count1_removed < remove1:
        count1_removed += 1
    else:
        result.append(char)

# 결과 리스트 역순 (효율성을 위해 한 번에 뒤집기)
result.reverse()

# '0' 제거 (뒤에서부터 절반)
final_result = []
count0_removed = 0
for char in result:
    if char == '0' and count0_removed < remove0:
        count0_removed += 1
    else:
        final_result.append(char)

# 최종 결과를 다시 역순으로 출력
final_result.reverse()
print(''.join(final_result))