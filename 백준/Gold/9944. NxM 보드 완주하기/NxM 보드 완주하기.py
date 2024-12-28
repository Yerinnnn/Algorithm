import sys
sys.setrecursionlimit(10**7)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상, 우, 하, 좌
case_number = 1  # 테스트 케이스 번호

def is_filled():
    """
    격자판의 모든 빈 칸이 채워졌는지 확인
    """
    for row in board:
        if "." in row:
            return False
    return True

def backtrack(x, y, moves):
    """
    백트래킹 함수
    - x, y: 현재 위치
    - moves: 현재까지 이동 횟수
    """
    global min_moves

    # 모든 칸을 방문한 경우 최소 이동 횟수 갱신
    if is_filled():
        min_moves = min(min_moves, moves)
        return

    # 현재 이동 횟수가 최소 이동 횟수보다 큰 경우 탐색 중단
    if moves >= min_moves:
        return

    for dx, dy in directions:
        nx, ny = x, y
        path = []  # 이번 방향으로 이동한 경로

        # 현재 방향으로 최대한 이동
        while 0 <= nx + dx < N and 0 <= ny + dy < M and board[nx + dx][ny + dy] == ".":
            nx += dx
            ny += dy
            board[nx][ny] = "*"  # 이동 경로를 채움
            path.append((nx, ny))

        # 경로가 있다면 재귀 호출
        if path:
            backtrack(nx, ny, moves + 1)

            # 백트래킹: 경로 복구
            for px, py in path:
                board[px][py] = "."

while True:
    try:
        N, M = map(int, input().split())
        board = [list(input().strip()) for _ in range(N)]

        # 초기화
        min_moves = float("inf")

        # 모든 가능한 시작점에서 탐색
        for i in range(N):
            for j in range(M):
                if board[i][j] == ".":
                    board[i][j] = "*"  # 시작점 설정
                    backtrack(i, j, 0)
                    board[i][j] = "."  # 시작점 복구

        if min_moves == float("inf"):  # 모든 경로를 탐색할 수 없는 경우
            print(f"Case {case_number}: -1")
        else:
            print(f"Case {case_number}: {min_moves}")

        case_number += 1
    except:
        break