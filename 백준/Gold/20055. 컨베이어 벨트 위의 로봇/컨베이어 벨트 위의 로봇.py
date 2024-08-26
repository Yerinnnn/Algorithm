from collections import deque

# n: 컨베이어 벨트의 길이, k: 종료 조건에 필요한 내구도 0의 칸 개수
n, k = map(int, input().split())

# 컨베이어 벨트의 내구도 정보를 deque로 초기화
a = deque(map(int, input().split()))

# 로봇의 위치를 나타내는 deque 초기화, 처음엔 모든 칸이 비어있음 (0)
robot = deque([0] * n)

# 결과를 저장할 변수 초기화
result = 0

# 시뮬레이션 반복
while True:
    # 1단계: 벨트가 한 칸 회전함
    result += 1  # 단계 수를 증가
    a.rotate(1)  # 벨트의 내구도 정보가 한 칸 회전
    robot[-1] = 0  # 회전 후 내리는 위치의 로봇을 제거
    robot.rotate(1)  # 로봇의 위치 정보가 한 칸 회전
    robot[-1] = 0  # 회전 후 내리는 위치의 로봇을 제거

    # 2단계: 로봇이 이동함 (뒤에서부터 앞으로)
    for i in range(n - 2, -1, -1):  # 뒤에서부터 로봇을 확인
        # 앞 칸에 로봇이 없고, 내구도가 1 이상 남아있으며, 현재 칸에 로봇이 있는 경우
        if a[i + 1] >= 1 and robot[i + 1] == 0 and robot[i] == 1:
            robot[i + 1] = 1  # 로봇이 다음 칸으로 이동
            robot[i] = 0  # 현재 칸은 비어있게 됨
            a[i + 1] -= 1  # 이동한 칸의 내구도를 1 감소
    robot[-1] = 0  # 로봇이 내리는 위치에 도달하면 제거

    # 3단계: 로봇이 올라가는 위치에 로봇을 올림
    if a[0] != 0 and robot[0] != 1:  # 내구도가 남아있고, 로봇이 없는 경우
        robot[0] = 1  # 로봇을 올림
        a[0] -= 1  # 올린 위치의 내구도를 1 감소

    # 4단계: 내구도가 0인 칸의 개수가 k개 이상이면 종료
    if a.count(0) >= k:
        break

# 시뮬레이션이 종료된 후 결과 출력
print(result)