T = int(input())

# dp 배열 초기화: dp[i]는 i를 1, 2, 3의 합으로 나타내는 경우의 수를 의미
dp = [1] * 10001  # 모든 값을 1로 초기화, i를 1로만 만드는 경우 포함

# 2를 사용하는 경우의 수 추가
# dp[i]는 dp[i-2]에서 2를 더해준 경우의 수를 더함
for i in range(2, 10001):
    dp[i] += dp[i-2]

# 3을 사용하는 경우의 수 추가
# dp[i]는 dp[i-3]에서 3을 더해준 경우의 수를 더함
for i in range(3, 10001):
    dp[i] += dp[i-3]

# 각 테스트 케이스마다 n을 입력받아, 해당 n에 대한 경우의 수를 출력
for _ in range(T):
    n = int(input())
    print(dp[n])