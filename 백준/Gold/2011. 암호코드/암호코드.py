message = input().strip()
MOD = 1000000  # 결과를 나눌 값

# 예외 처리: 처음이 '0'인 경우 디코딩 불가능
if message[0] == '0':
    print(0)
else:
    n = len(message)
    dp = [0] * (n + 1)  # dp 배열 초기화
    dp[0] = 1  # 빈 문자열의 경우의 수는 1
    dp[1] = 1  # 첫 번째 문자가 유효한 경우의 수는 1

    # DP 계산
    for i in range(2, n + 1):
        current = int(message[i - 1])  # 현재 문자
        prev = int(message[i - 2])  # 이전 문자

        # 현재 문자가 유효한 경우 (1 ~ 9)
        if 1 <= current <= 9:
            dp[i] += dp[i - 1]
            dp[i] %= MOD  # 모듈로 연산 적용

        # 이전 문자와 결합하여 유효한 경우 (10 ~ 26)
        if 10 <= prev * 10 + current <= 26:
            dp[i] += dp[i - 2]
            dp[i] %= MOD  # 모듈로 연산 적용

    print(dp[n])