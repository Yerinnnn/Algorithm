def solution(n, times):
    # 가장 적은 시간과 가장 많은 시간 초기화
    left = 1
    right = max(times) * n
    
    # 이진 탐색
    while left <= right:
        mid = (left + right) // 2  # 중간 시간 계산
        
        # 현재 시간에 심사 가능한 총 인원 수 계산
        total_people = sum(mid // time for time in times)
        
        # 총 인원 수가 n 이상이면 현재 시간이 충분하거나 과도함
        if total_people >= n:
            right = mid - 1  # 시간을 줄여서 더 적합한 시간 찾기
        else:
            left = mid + 1  # 시간을 늘려서 충분한 인원 수 찾기
    
    return left  # 최적의 최소 시간 반환