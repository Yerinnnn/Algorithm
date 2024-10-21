import sys
from collections import Counter

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

# 행 또는 열을 정렬하는 함수
def sort_and_count(matrix):
    max_len = 0
    new_matrix = []
    
    # 각 행(또는 열)에 대해 등장하는 숫자의 개수를 세고 정렬
    for row in matrix:
        count = Counter(row)
        if count.get(0): del count[0]  # 0은 무시
        sorted_row = sorted(count.items(), key=lambda x: (x[1], x[0]))  # 등장 횟수와 숫자 크기 순으로 정렬
        new_row = []
        for num, cnt in sorted_row:
            new_row.extend([num, cnt])
        max_len = max(max_len, len(new_row))  # 가장 긴 행의 길이를 기록
        new_matrix.append(new_row)
    
    # 길이가 짧은 행을 0으로 채워서 최대 길이에 맞춤
    for row in new_matrix:
        row.extend([0] * (max_len - len(row)))
        if len(row) > 100:  # 길이가 100을 넘으면 자르기
            row = row[:100]
    
    return new_matrix

# R 연산: 행 기준으로 정렬
def r_operation():
    global A
    A = sort_and_count(A)

# C 연산: 열 기준으로 정렬
def c_operation():
    global A
    A = list(zip(*A))  # 배열을 전치 (행과 열을 뒤바꿈)
    A = sort_and_count(A)  # 전치된 배열에 대해 R 연산 적용
    A = list(zip(*A))  # 다시 원래 배열로 전치

# 연산 실행
time = 0
while time <= 100:
    if len(A) >= r and len(A[0]) >= c and A[r-1][c-1] == k:  # 목표 좌표의 값이 k와 일치하면 종료
        print(time)
        break
    
    if len(A) >= len(A[0]):  # 행이 더 많거나 같으면 R 연산
        r_operation()
    else:  # 열이 더 많으면 C 연산
        c_operation()
    
    time += 1

if time > 100:
    print(-1)  # 100초 안에 못 찾으면 -1 출력