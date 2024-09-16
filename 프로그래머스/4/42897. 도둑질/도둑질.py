def solution(money):
    n = len(money)
    
    # 경우 1: 첫 집을 훔치는 경우
    def calculate_max_money(start, end):
        dp = [0] * (end - start + 1)
        dp[0] = money[start]
        dp[1] = max(money[start], money[start + 1])
        
        for i in range(2, end - start + 1):
            dp[i] = max(dp[i-1], dp[i-2] + money[start + i])
        
        return dp[-1]
    
    # 첫 집을 훔치는 경우와 첫 집을 훔치지 않는 경우를 고려
    if n == 1:
        return money[0]
    elif n == 2:
        return max(money[0], money[1])
    else:
        return max(calculate_max_money(0, n-2), calculate_max_money(1, n-1))