from collections import deque
import sys
input = sys.stdin.readline

# 사무실의 세로(N), 가로(M)
N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]

# 방향: 남, 동, 북, 서 (시계 방향)
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

# CCTV별 감시 방향 설정
direction = {
    1: [[0], [1], [2], [3]],  # 1번 CCTV: 4방향 중 1방향
    2: [[0, 2], [1, 3]],      # 2번 CCTV: 두 방향(상하 or 좌우)
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],  # 3번 CCTV: 두 직각 방향
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],  # 4번 CCTV: 세 방향
    5: [[0, 1, 2, 3]]  # 5번 CCTV: 네 방향 모두
}

# 범위 체크
def check(row, col):
    return row < 0 or row >= N or col < 0 or col >= M

# CCTV와 빈칸을 초기화
def init():
    obj = deque()  # cctv 위치 큐
    answer = 0
    for i in range(N):
        for j in range(M):
            if space[i][j] != 6 and space[i][j] != 0:
                obj.append((space[i][j], i, j))  # cctv 번호와 위치 저장
            if space[i][j] == 0:
                answer += 1  # 빈칸 갯수 카운트
    return obj, answer

# CCTV 이동 처리
def move(y, x, direc, space_copy):
    for d in direc:
        ny, nx = y, x
        while True:
            nx += dx[d]
            ny += dy[d]
            if check(ny, nx) or space_copy[ny][nx] == 6:  # 범위를 벗어나거나 벽이면 종료
                break
            if space_copy[ny][nx] != 0:  # 빈칸이 아니면 계속 진행
                continue
            space_copy[ny][nx] = '#'  # 감시 범위를 표시

# 사각지대 크기 계산
def zero_cnt(space_copy):
    global answer
    cnt = 0
    for i in space_copy:
        cnt += i.count(0)
    answer = min(answer, cnt)

# 백트래킹을 이용한 DFS
def dfs(level, space):
    space_copy = [[j for j in space[i]] for i in range(N)]  # 깊은 복사
    if level == len(cctv):  # 모든 CCTV 처리 완료
        zero_cnt(space_copy)
        return

    number, y, x = cctv[level]  # 현재 처리할 CCTV 정보
    for d in direction[number]:  # 각 CCTV의 가능한 방향에 대해 처리
        move(y, x, d, space_copy)  # CCTV 이동
        dfs(level + 1, space_copy)  # 다음 CCTV 처리
        space_copy = [[j for j in space[i]] for i in range(N)]  # 복원

# 초기화
cctv, answer = init()
dfs(0, space)
print(answer)