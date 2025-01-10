import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 재귀 제한 늘리기

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]  # 방문하지 않은 곳은 -1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    # 도착점에 도달하면 1을 반환
    if x == M-1 and y == N-1:
        return 1
    
    # 이미 방문한 적이 있다면 그 위치에서의 경로 수를 반환
    if dp[x][y] != -1:
        return dp[x][y]
    
    # 현재 위치에서 시작하는 경로 수를 0으로 초기화
    dp[x][y] = 0
    
    # 상하좌우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 범위 내이고 현재보다 낮은 곳으로만 이동
        if 0 <= nx < M and 0 <= ny < N and board[x][y] > board[nx][ny]:
            dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]

print(dfs(0, 0))