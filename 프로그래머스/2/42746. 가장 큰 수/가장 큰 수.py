from functools import cmp_to_key

def compare(a, b):
    # 두 숫자를 이어 붙였을 때 더 큰 숫자를 만드는 순서로 정렬하기 위해 비교 함수 정의
    if a + b > b + a:
        return -1  # a가 b 앞에 오도록 함
    elif a + b < b + a:
        return 1  # b가 a 앞에 오도록 함
    else:
        return 0  # a와 b가 동일한 순서로 정렬

def solution(numbers):
    # 숫자 리스트를 문자열로 변환
    numbers = list(map(str, numbers))
    
    # compare 함수를 기준으로 숫자들을 정렬
    numbers.sort(key=cmp_to_key(compare))
    
    # 정렬된 숫자들을 이어 붙여서 가장 큰 수를 생성
    answer = ''.join(numbers)
    
    # 결과가 0으로만 이루어졌다면 "0" 반환
    return answer if answer[0] != '0' else '0'