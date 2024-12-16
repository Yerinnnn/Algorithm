import sys
input = sys.stdin.readline

# 이동 방향 정의 (동, 서, 북, 남)
DIRECTION = [(0, 1), (0, -1), (-1, 0), (1, 0)]

# 주사위 면의 상태를 갱신하는 함수
def roll_dice(dice, direction):
    top, bottom, left, right, front, back = dice
    if direction == 1:  # 동쪽
        return [left, right, bottom, top, front, back]
    elif direction == 2:  # 서쪽
        return [right, left, top, bottom, front, back]
    elif direction == 3:  # 북쪽
        return [front, back, left, right, bottom, top]
    elif direction == 4:  # 남쪽
        return [back, front, left, right, top, bottom]

n, m, x, y, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

# 주사위 초기 상태 (6면: 윗면, 바닥면, 좌, 우, 앞, 뒤)
dice = [0, 0, 0, 0, 0, 0]

# 시뮬레이션 실행
for command in commands:
    dx, dy = DIRECTION[command - 1]  # 명령에 따른 방향 계산
    nx, ny = x + dx, y + dy  # 이동할 위치 계산

    # 격자판을 벗어나는 경우 명령 무시
    if not (0 <= nx < n and 0 <= ny < m):
        continue

    # 주사위 굴리기
    dice = roll_dice(dice, command)

    # 주사위와 격자판 값 갱신
    if grid[nx][ny] == 0:
        grid[nx][ny] = dice[1]  # 주사위 바닥면의 값이 격자판으로 복사
    else:
        dice[1] = grid[nx][ny]  # 격자판 값이 주사위 바닥면으로 복사
        grid[nx][ny] = 0  # 격자판 값 초기화

    # 주사위 위치 갱신
    x, y = nx, ny

    # 주사위 윗면 출력
    print(dice[0])