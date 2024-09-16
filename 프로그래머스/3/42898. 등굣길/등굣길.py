def solution(m, n, puddles):
    # DP 테이블 초기화
    dp = [[0] * n for _ in range(m)]
    
    # 장애물을 처리하기 위한 세트
    puddle_set = set(tuple(puddle) for puddle in puddles)
    
    # 시작 지점 초기화
    if (1, 1) not in puddle_set:
        dp[0][0] = 1
    
    # DP 테이블을 채우는 과정
    for i in range(m):
        for j in range(n):
            if (i + 1, j + 1) in puddle_set:
                # 장애물이 있는 위치는 경로 수가 0
                dp[i][j] = 0
            else:
                # 위쪽 또는 왼쪽에서 오는 경로 수를 더함
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
    
    # 목표 지점의 경로 수를 반환
    return dp[m - 1][n - 1] % 1_000_000_007