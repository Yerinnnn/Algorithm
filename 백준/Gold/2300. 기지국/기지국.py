N = int(input())
buildings = []
for _ in range(N):
    x, y = map(int, input().split())
    buildings.append((x, abs(y)))  # y는 절댓값으로 저장
buildings.sort()  # x좌표 기준 정렬

dp = [float('inf')] * (N + 1)  # dp[i]: i번째 건물까지 커버하는 최소 비용
dp[0] = 0

for i in range(N):  # 현재 위치
    max_height = 0  # 현재 구간의 최대 높이
    for j in range(i, N):  # 현재부터 끝까지
        max_height = max(max_height, buildings[j][1])  # 최대 높이 갱신
        # 현재 구간의 너비와 높이 중 큰 값이 기지국의 크기
        width = buildings[j][0] - buildings[i][0]
        size = max(width, max_height * 2)
        dp[j + 1] = min(dp[j + 1], dp[i] + size)

print(dp[N])