import sys
input = sys.stdin.readline
INF = float('inf')

n = int(input())
sx, sy = map(int, input().split())
points = [(sx, sy)]
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

dp = [[INF] * 5 for _ in range(n+1)]
dp[0][0] = 0

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

for i in range(n):
    x1, y1 = points[i]
    x2, y2 = points[i+1]
    for now in range(5):
        if dp[i][now] == INF:
            continue
        nx1, ny1 = x1 + dx[now], y1 + dy[now]
        if not (0 <= nx1 <= 100000 and 0 <= ny1 <= 100000):
            continue
        for nxt in range(5):
            nx2, ny2 = x2 + dx[nxt], y2 + dy[nxt]
            if not (0 <= nx2 <= 100000 and 0 <= ny2 <= 100000):
                continue
            dist = dp[i][now] + abs(nx1 - nx2) + abs(ny1 - ny2)
            dp[i+1][nxt] = min(dp[i+1][nxt], dist)

print(min(dp[n]))