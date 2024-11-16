for test_case in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    view_count = 0  # 조망권 확보 세대의 총합

    for i in range(2, N-2):
        max_neighbor_height = max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])
        if buildings[i] > max_neighbor_height:
            view_count += buildings[i] - max_neighbor_height  # 조망권 세대 높이 계산

    print(f"#{test_case} {view_count}")