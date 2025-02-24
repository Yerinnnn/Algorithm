import sys
sys.setrecursionlimit(10**6)

def solve(n, p, q, x, y, dp):
    if n <= 0:
        return 1
       
    if n in dp:
        return dp[n]
       
    dp[n] = solve(n//p - x, p, q, x, y, dp) + solve(n//q - y, p, q, x, y, dp)
    return dp[n]

n, p, q, x, y = map(int, input().split())
dp = {}  # n이 매우 크므로 딕셔너리로 dp 테이블 구현
print(solve(n, p, q, x, y, dp))