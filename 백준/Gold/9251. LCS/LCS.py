def longest_common_subsequence(A, B):
    n = len(A)
    m = len(B)

    # DP 테이블 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # DP 계산
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:  # 문자가 같은 경우
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # 문자가 다른 경우
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # 최장 공통 부분 수열의 길이 반환
    return dp[n][m]

A = input().strip()
B = input().strip()

print(longest_common_subsequence(A, B))