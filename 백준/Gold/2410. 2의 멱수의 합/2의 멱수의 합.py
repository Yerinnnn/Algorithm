import sys

N = int(sys.stdin.readline().strip())

# N보다 작거나 같은 2의 제곱수 구하기
powers = []
power = 1  # 2^0 = 1부터 시작
while power <= N:
    powers.append(power)
    power *= 2
    
dp = [0] * (N + 1)
dp[0] = 1  # 아무것도 선택하지 않는 경우 1가지

MOD = 1_000_000_000

for power in powers:
    for i in range(power, N + 1):  
        dp[i] = (dp[i] + dp[i - power]) % MOD

print(dp[N])