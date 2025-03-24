import sys

input = sys.stdin.readline
n, m = map(int, input().split())
array = list(map(int, input().split()))

# 이분 탐색
start, end = 0, max(array) - min(array)  # 최소 차이 0, 최대 차이 배열의 최댓값-최솟값
answer = end

while start <= end:
    mid = (start + end) // 2  # 현재 기준 차이값
    
    # 구간 나누기
    count = 1  # 구간 수 (첫 번째 구간부터 시작)
    min_value, max_value = array[0], array[0]  # 현재 구간의 최솟값, 최댓값 초기화
    
    for i in range(1, n):
        # 현재 구간에 포함시킬지 새 구간을 시작할지 결정
        current_min = min(min_value, array[i])
        current_max = max(max_value, array[i])
        
        # 현재 값을 포함했을 때 차이가 기준(mid)보다 크면 새 구간 시작
        if current_max - current_min > mid:
            count += 1
            min_value = max_value = array[i]  # 새 구간 시작
        else:
            # 현재 구간에 포함
            min_value = current_min
            max_value = current_max
    
    # 구간 수에 따라 이분 탐색 방향 결정
    if count > m:  # 구간이 너무 많으면 기준 차이를 늘림
        start = mid + 1
    else:  # 구간이 m 이하면 기준 차이를 줄여봄
        answer = min(answer, mid)  # 가능한 답 갱신
        end = mid - 1

print(answer)