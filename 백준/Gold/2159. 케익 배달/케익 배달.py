import sys
input = sys.stdin.readline  # 빠른 입력
INF = float('inf')  # 무한대 값

# 입력: 케이크 개수, 시작 위치
n = int(input())
sx, sy = map(int, input().split())
points = [(sx, sy)]  # 시작점 포함한 모든 위치 저장
for _ in range(n):
   x, y = map(int, input().split())
   points.append((x, y))

# dp[i][j]: i번째 케이크를 j방향으로 받을 때의 최소 이동 거리
dp = [[INF] * 5 for _ in range(n+1)]
dp[0][0] = 0  # 시작점 초기화

# 5가지 방향: 현재위치, 상, 하, 좌, 우
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

# 각 케이크 위치마다
for i in range(n):
   x1, y1 = points[i]    # 현재 케이크 기준 위치
   x2, y2 = points[i+1]  # 다음 케이크 기준 위치
   
   # 현재 위치의 5가지 방향에 대해
   for now in range(5):
       if dp[i][now] == INF:  # 현재 위치에 도달할 수 없으면 스킵
           continue
       
       # 현재 실제 위치 계산
       nx1, ny1 = x1 + dx[now], y1 + dy[now]
       # 범위 체크 (0 ≤ x,y ≤ 100,000)
       if not (0 <= nx1 <= 100000 and 0 <= ny1 <= 100000):
           continue
           
       # 다음 위치의 5가지 방향에 대해
       for nxt in range(5):
           # 다음 실제 위치 계산
           nx2, ny2 = x2 + dx[nxt], y2 + dy[nxt]
           # 범위 체크
           if not (0 <= nx2 <= 100000 and 0 <= ny2 <= 100000):
               continue
               
           # 현재까지의 최소 거리 + 현재위치에서 다음위치까지 거리
           dist = dp[i][now] + abs(nx1 - nx2) + abs(ny1 - ny2)
           # 최소값 갱신
           dp[i+1][nxt] = min(dp[i+1][nxt], dist)

# 마지막 케이크에서의 5가지 방향 중 최소값 출력
print(min(dp[n]))