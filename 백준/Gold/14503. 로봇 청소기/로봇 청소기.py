import sys
input = sys.stdin.readline

# 방향 벡터: 북, 동, 남, 서 (반시계 방향으로 회전 시 사용)
DIRECTION = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def simulate_cleaning(grid, r, c, d):
    n, m = len(grid), len(grid[0])  # 격자의 크기
    visited = [[False] * m for _ in range(n)]  # 청소 여부를 기록할 배열
    cleaned_count = 0

    while True:
        # 1. 현재 위치 청소
        if not visited[r][c]:  # 아직 청소하지 않은 경우
            visited[r][c] = True
            cleaned_count += 1

        # 2. 주변 4칸 중 청소되지 않은 칸이 있는지 확인
        found_cleanable = False
        for _ in range(4):
            d = (d - 1) % 4  # 반시계 방향으로 회전
            nr, nc = r + DIRECTION[d][0], c + DIRECTION[d][1]

            # 이동 가능한지 확인: 범위 내, 빈 칸이며 아직 청소되지 않은 칸
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0 and not visited[nr][nc]:
                r, c = nr, nc  # 이동
                found_cleanable = True
                break

        # 3. 청소되지 않은 칸이 없다면 후진
        if not found_cleanable:
            back_d = (d + 2) % 4  # 현재 방향의 반대 방향
            r_back, c_back = r + DIRECTION[back_d][0], c + DIRECTION[back_d][1]

            # 후진할 수 없는 경우 작동 종료
            if grid[r_back][c_back] == 1:
                break
            r, c = r_back, c_back  # 후진

    return cleaned_count

n, m = map(int, input().split())  # 격자의 크기
r, c, d = map(int, input().split())  # 로봇 청소기의 초기 위치와 방향
grid = [list(map(int, input().split())) for _ in range(n)]  # 격자 입력

# 시뮬레이션 실행 및 결과 출력
result = simulate_cleaning(grid, r, c, d)
print(result)