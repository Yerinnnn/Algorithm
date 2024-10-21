n = int(input())  # 아이들의 수
arr = list(map(int, input().split()))  # 번호 리스트

# DP 배열을 사용
# 가장 긴 증가하는 부분 수열의 길이를 계산
dp = [0] * (n + 1)  # 각 번호가 몇 번째 위치에 있을 수 있는지 기록
max_len = 0

for num in arr:
    dp[num] = dp[num - 1] + 1  # 이전 번호의 위치에 이어서 번호를 추가
    max_len = max(max_len, dp[num])  # 가장 긴 증가하는 부분 수열의 길이 갱신

# 이동해야 하는 횟수는 전체 아이들의 수 - 가장 긴 증가하는 부분 수열의 길이
print(n - max_len)