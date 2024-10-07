def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)  # 기울기 계산


N = int(input())  # 빌딩의 개수를 입력 받음

# 빌딩의 높이를 입력받아 리스트로 변환
buildings = list(map(int, input().split()))

result = 0  # 보이는 빌딩의 최대 개수를 저장할 변수
# 각 빌딩에 대해 반복
for i1, y1 in enumerate(buildings):
    x1 = i1 + 1  # 현재 빌딩의 x좌표 (1부터 시작)

    # 오른쪽에서 볼 수 있는 빌딩 수를 계산
    cur_slope_right = None  # 현재까지의 최대 기울기 초기화
    visible_right = 0  # 오른쪽에서 보이는 빌딩 개수 초기화

    # 오른쪽으로 탐색
    for i2 in range(i1 + 1, N + 1):
        if i2 == N: break  # 범위를 초과할 경우 종료
        x2 = i2 + 1  # 오른쪽 빌딩의 x좌표
        y2 = buildings[i2]  # 오른쪽 빌딩의 높이
        slope_right = slope(x1, y1, x2, y2)  # 오른쪽 기울기 계산

        # 현재 기울기가 이전의 기울기보다 크면
        if cur_slope_right is None or cur_slope_right < slope_right:
            cur_slope_right = slope_right  # 기울기 업데이트
            visible_right += 1  # 보이는 빌딩 개수 증가

    # 왼쪽에서 볼 수 있는 빌딩 수를 계산
    cur_slope_left = None  # 현재까지의 최대 기울기 초기화
    visible_left = 0  # 왼쪽에서 보이는 빌딩 개수 초기화

    # 왼쪽으로 탐색
    for i3 in range(i1 - 1, -1, -1):
        if i3 == -1: break  # 범위를 초과할 경우 종료
        x2 = i3 + 1  # 왼쪽 빌딩의 x좌표
        y2 = buildings[i3]  # 왼쪽 빌딩의 높이
        slope_left = slope(x1, y1, x2, y2)  # 왼쪽 기울기 계산

        # 현재 기울기가 이전의 기울기보다 크면
        if cur_slope_left is None or cur_slope_left > slope_left:
            cur_slope_left = slope_left  # 기울기 업데이트
            visible_left += 1  # 보이는 빌딩 개수 증가

    # 현재 빌딩에서 보이는 빌딩의 총 개수를 계산
    if (visible_left + visible_right) > result:
        result = visible_left + visible_right  # 최대값 업데이트

print(result)