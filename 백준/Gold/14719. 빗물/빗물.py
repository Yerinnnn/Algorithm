import sys

input = sys.stdin.readline

h, w = map(int, input().split())  # h: 블록의 최대 높이, w: 블록의 개수
world = list(map(int, input().split()))  # 블록의 높이 리스트

# 왼쪽과 오른쪽에서의 최대 높이를 저장할 리스트
left_max = [0] * w
right_max = [0] * w

# 왼쪽에서의 최대 높이 계산
left_max[0] = world[0]
for i in range(1, w):
    left_max[i] = max(left_max[i - 1], world[i])

# 오른쪽에서의 최대 높이 계산
right_max[w - 1] = world[w - 1]
for i in range(w - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], world[i])

# 빗물의 양 계산
total_water = 0
for i in range(1, w - 1):
    # 현재 위치에서의 최대 높이는 왼쪽과 오른쪽에서의 최대 높이 중 최소값
    water_height = min(left_max[i], right_max[i]) - world[i]
    if water_height > 0:
        total_water += water_height

print(total_water)