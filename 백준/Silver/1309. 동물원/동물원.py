N = int(input())
MOD = 9901

# dp[i][j]: i번째 줄에서 j상태일 때의 경우의 수
# j: 0(빈칸), 1(왼쪽), 2(오른쪽)
dp = [[0]*3 for _ in range(N+1)]

# 초기화: 첫 번째 줄
dp[1] = [1, 1, 1]

# 두 번째 줄부터
for i in range(2, N+1):
   # 현재 줄이 빈칸
   dp[i][0] = sum(dp[i-1]) % MOD
   # 현재 줄 왼쪽에 사자
   dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD
   # 현재 줄 오른쪽에 사자
   dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % MOD

print(sum(dp[N]) % MOD)