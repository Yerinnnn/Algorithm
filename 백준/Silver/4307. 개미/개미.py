import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # 막대 길이 l, 개미 수 n
    l, n = map(int, input().split())
    
    min_time = 0  # 최소 시간
    max_time = 0  # 최대 시간
    
    for _ in range(n):
        # 개미의 위치 pos
        pos = int(input())
        # 각 개미의 가장 가까운 끝점까지의 거리
        time_to_end = min(pos, l - pos)
        min_time = max(min_time, time_to_end)
        
        # 각 개미의 가장 먼 끝점까지의 거리
        time_to_far = max(pos, l - pos)
        max_time = max(max_time, time_to_far)
    
    print(min_time, max_time)