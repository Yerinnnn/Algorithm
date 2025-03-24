import sys
input = sys.stdin.readline

# 각 난이도별 문제 수
e, em, m, mh, h = map(int, input().split())
    
# 이분 탐색
# 최소 0개, 최대 각 유형별 최대 사용 가능 수의 최솟값
start, end = 0, min(e + em, em + m + mh, mh + h)
    
while start <= end:
    mid = (start + end) // 2  # 개최 가능한 대회 수
        
    # 각 난이도별 필요한 문제 수
    easy_needed = mid
    mid_needed = mid
    hard_needed = mid
        
    # 쉬운 문제
    if e >= easy_needed:  # 쉬운 문제만으로 충분한 경우
        easy_em_used = 0
    else:
        # 쉬운 문제가 부족하면 쉬운-중간 문제로 보충
        easy_em_used = easy_needed - e
        if easy_em_used > em:  # 쉬운-중간 문제도 부족하면 불가능
            end = mid - 1
            continue
        
    # 어려운 문제
    if h >= hard_needed:  # 어려운 문제만으로 충분한 경우
        hard_mh_used = 0
    else:
        # 어려운 문제가 부족하면 중간-어려운 문제로 보충
        hard_mh_used = hard_needed - h
        if hard_mh_used > mh:  # 중간-어려운 문제도 부족하면 불가능
            end = mid - 1
            continue
        
    # 중간 문제
    em_left = em - easy_em_used  # 남은 쉬운-중간 문제
    mh_left = mh - hard_mh_used  # 남은 중간-어려운 문제
        
    # 중간 문제 커버 가능 여부 확인
    # 남은 쉬운-중간 문제 + 중간 문제 + 남은 중간-어려운 문제로 중간 난이도 채울 수 있는지
    if em_left + m + mh_left >= mid_needed:
        # 중간 난이도도 커버 가능하면 더 많은 대회 시도
        start = mid + 1
    else:
        # 중간 난이도 커버 불가능하면 더 적은 대회로 시도
        end = mid - 1
    
print(end)