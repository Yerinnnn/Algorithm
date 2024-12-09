from collections import deque

# 톱니바퀴 회전 함수
def rotate_gears(gears, gear_idx, direction):
    # 톱니바퀴의 회전 여부와 방향 저장
    rotations = [0] * 4
    rotations[gear_idx] = direction  # 명령받은 톱니바퀴의 회전 방향

    # 왼쪽으로 전파
    for i in range(gear_idx, 0, -1):
        if gears[i][6] != gears[i-1][2]:  # 맞닿은 톱니의 극이 다르면
            rotations[i-1] = -rotations[i]  # 반대 방향으로 회전
        else:
            break  # 회전이 멈춤

    # 오른쪽으로 전파
    for i in range(gear_idx, 3):
        if gears[i][2] != gears[i+1][6]:  # 맞닿은 톱니의 극이 다르면
            rotations[i+1] = -rotations[i]  # 반대 방향으로 회전
        else:
            break  # 회전이 멈춤

    # 회전 적용
    for i in range(4):
        if rotations[i] == 1:  # 시계 방향 회전
            gears[i].rotate(1)
        elif rotations[i] == -1:  # 반시계 방향 회전
            gears[i].rotate(-1)

# 점수 계산 함수
def calculate_score(gears):
    score = 0
    for i in range(4):
        if gears[i][0] == '1':  # 12시 방향이 S극인 경우
            score += 2 ** i  # 2의 i승 점수 추가
    return score

gears = [deque(input().strip()) for _ in range(4)]  # 톱니바퀴 상태 입력
k = int(input())  # 회전 명령의 개수

# 회전 명령 처리
for _ in range(k):
    gear_idx, direction = map(int, input().split())
    rotate_gears(gears, gear_idx - 1, direction)  # 1-based 인덱스를 0-based로 변환

print(calculate_score(gears))