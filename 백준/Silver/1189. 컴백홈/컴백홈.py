R, C, K = map(int, input().split())
board = [list(input()) for _ in range(R)]

def dfs(x, y, dist):
    if dist == K:
        if x == 0 and y == C-1:
            return 1
        return 0
    
    count = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != 'T':
            board[nx][ny] = 'T'
            count += dfs(nx, ny, dist+1)
            board[nx][ny] = '.'
    return count
    
board[R-1][0] = 'T'
print(dfs(R-1, 0, 1))