from collections import deque
import sys
input = sys.stdin.readline

def process_commands(p, n, arr):
    reverse = False  # 뒤집힘 여부를 나타내는 플래그
    dq = deque(arr)  # 배열을 deque로 변환

    for command in p:
        if command == 'R':  # 뒤집기 명령
            reverse = not reverse
        elif command == 'D':  # 첫 번째 원소 삭제
            if not dq:  # 덱이 비어있으면 에러 발생
                return "error"
            if reverse:
                dq.pop()  # 뒤집힌 상태라면 마지막 원소 제거
            else:
                dq.popleft()  # 정상 상태라면 첫 번째 원소 제거

    if reverse:  # 뒤집힌 상태면 결과도 뒤집어서 출력
        dq.reverse()
    return "[" + ",".join(map(str, dq)) + "]"

T = int(input())
for _ in range(T):
    p = input().strip()  # 명령어 문자열
    n = int(input())  # 배열의 길이
    arr_input = input().strip()[1:-1]  # 배열 입력 문자열에서 [] 제거

    if arr_input:  # 배열이 비어있지 않은 경우
        arr = list(map(int, arr_input.split(",")))
    else:  # 빈 배열인 경우
        arr = []

    result = process_commands(p, n, arr)
    print(result)