T = int(input())

for test_case in range(1, T + 1):
    # 재료의 수 N, 제한 칼로리 L
    N, L = map(int, input().split())
    
    ingredients = []
    # 점수와 칼로리
    for _ in range(N):
        T, K = map(int, input().split())
        ingredients.append((T, K))
        
    dp = [0] * (L + 1)
    
    for T, K in ingredients:
        for cal in range(L, K-1, -1):
            dp[cal] = max(dp[cal], dp[cal - K] + T)
            
    print(f"#{test_case} {dp[L]}")