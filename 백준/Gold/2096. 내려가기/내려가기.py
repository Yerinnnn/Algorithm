import sys
input = sys.stdin.readline

n = int(input())  # 행의 개수
max_dp = [0] * 3  # 최대값 계산용 DP 배열
min_dp = [0] * 3  # 최소값 계산용 DP 배열

# 첫 번째 행 입력
first_row = list(map(int, input().split()))
max_dp[:] = first_row  # 첫 행의 값으로 초기화
min_dp[:] = first_row  # 첫 행의 값으로 초기화

for _ in range(1, n):
    row = list(map(int, input().split()))  # 현재 행 입력
    prev_max = max_dp[:]  # 이전 최대값 DP 상태 저장
    prev_min = min_dp[:]  # 이전 최소값 DP 상태 저장

    # 최대값 갱신
    max_dp[0] = row[0] + max(prev_max[0], prev_max[1])
    max_dp[1] = row[1] + max(prev_max[0], prev_max[1], prev_max[2])
    max_dp[2] = row[2] + max(prev_max[1], prev_max[2])

    # 최소값 갱신
    min_dp[0] = row[0] + min(prev_min[0], prev_min[1])
    min_dp[1] = row[1] + min(prev_min[0], prev_min[1], prev_min[2])
    min_dp[2] = row[2] + min(prev_min[1], prev_min[2])

print(max(max_dp), min(min_dp))