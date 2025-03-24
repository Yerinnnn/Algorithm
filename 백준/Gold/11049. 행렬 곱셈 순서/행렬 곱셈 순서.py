import sys

input = sys.stdin.readline

# 행렬 개수
n = int(input())

# 행렬 크기 정보
array = [list(map(int, input().split())) for _ in range(n)]

# DP 테이블 초기화 : dp[i][j]는 i ~ j 번째 행렬 곱의 최솟값
dp = [[0] * n for _ in range(n)]

# 대각선 방향으로 DP 테이블 채우기 (간격 늘려가며 계산)
for diagonal in range(1, n):  # 대각선 간격
    for i in range(n - diagonal):  # 시작 행렬
        j = i + diagonal  # 끝 행렬

        # 최댓값으로 초기화 (2^31-1)
        dp[i][j] = (2**31) - 1

        # i부터 j까지의 행렬 곱에서 k를 기준으로 분할하여 최소 연산 횟수 계산
        for k in range(i, j):
            # (i~k 구간 연산 비용) + (k+1~j 구간 연산 비용) + (두 결과 행렬의 곱셈 비용)
            cost = dp[i][k] + dp[k + 1][j] + array[i][0] * array[k][1] * array[j][1]
            
            # 최소 비용 갱신
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][n - 1])