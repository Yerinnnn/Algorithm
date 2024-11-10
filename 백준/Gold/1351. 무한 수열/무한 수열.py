import sys
input = sys.stdin.readline

n, p, q = map(int, input().split())

# 메모이제이션을 위한 딕셔너리
dp = {0: 1}

# 재귀 함수 정의
def infinite_sequence(x):
    if x in dp:
        return dp[x]
    
    # 재귀적으로 a(x) 계산
    dp[x] = infinite_sequence(x // p) + infinite_sequence(x // q)
    return dp[x]

print(infinite_sequence(n))