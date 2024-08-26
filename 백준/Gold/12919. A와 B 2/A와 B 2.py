s = input()
t = input()

answer = 0

# 재귀 함수 sub 정의: str1이 s이고 target이 t로 초기화됨
def sub(str1, target):
    global answer  # 함수 내에서 answer 값을 변경하기 위해 global 선언
    
    # 두 문자열의 길이가 같아진 경우
    if len(str1) == len(target):
        # 두 문자열이 동일하면 answer를 1로 설정 (변환 가능)
        if target == str1:
            answer = 1
        return  # 더 이상 재귀 호출을 진행하지 않음
    
    # target의 마지막 글자가 'A'인 경우
    if target[-1] == 'A':
        # 마지막 글자 'A'를 제거하고 재귀 호출
        sub(str1, target[:-1])
    
    # target의 첫 번째 글자가 'B'인 경우
    if target[0] == 'B':
        # target을 역순으로 뒤집고 첫 글자 'B'를 제거하여 재귀 호출
        sub(str1, target[:0:-1])

# 변환 가능성을 체크하기 위해 초기 문자열 s와 목표 문자열 t로 함수 호출
sub(s, t)

# 변환 가능 여부 출력 (1이면 변환 가능, 0이면 불가능)
print(answer)