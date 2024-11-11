import sys
input = sys.stdin.readline

# 8방향 이동 (상, 하, 좌, 우, 대각선)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
              (-1, -1), (-1, 1), (1, -1), (1, 1)]

# 격자의 크기 N, M과 신이 좋아하는 문자열의 개수 K
n, m, k = map(int, input().split())
grid = [input().strip() for _ in range(n)]
queries = [input().strip() for _ in range(k)]

# 각 문자열을 찾은 횟수
result = {query: 0 for query in queries}

# 격자판에서 문자열 탐색 함수
def dfs(x, y, current_str):
    if current_str in result:
        result[current_str] += 1
    
    # 문자열이 최장 길이인 max_length에 도달하면 종료
    if len(current_str) == max_length:
        return

    # 8방향 탐색
    for dx, dy in directions:
        nx = (x + dx) % n
        ny = (y + dy) % m
        dfs(nx, ny, current_str + grid[nx][ny])

# 가장 긴 쿼리 문자열의 길이
max_length = max(len(query) for query in queries)

# 격자판의 모든 위치에서 문자열 탐색 시작
for i in range(n):
    for j in range(m):
        dfs(i, j, grid[i][j])

for query in queries:
    print(result[query])