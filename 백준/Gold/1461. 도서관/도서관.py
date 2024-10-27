n, m = map(int, input().split())  # 책의 개수 N, 세준이가 한 번에 들 수 있는 책의 개수 M
positions = list(map(int, input().split()))  # 책의 위치

# 음수와 양수 위치를 나누기
negative = sorted([x for x in positions if x < 0])
positive = sorted([x for x in positions if x > 0], reverse=True)

# 가장 멀리 있는 위치를 따로 기록
farthest_distance = max(abs(negative[0]) if negative else 0, positive[0] if positive else 0)

# 총 이동 거리 초기화
total_distance = 0

# 음수 위치에서 그룹화하여, 이동 거리 계산
for i in range(0, len(negative), m):
    total_distance += abs(negative[i]) * 2  # 왕복 이동

# 양수 위치에서 그룹화하여 이동 거리 계산
for i in range(0, len(positive), m):
    total_distance += positive[i] * 2

# 마지막 이동에서는 다시 돌아올 필요가 없기 때문에
# 가장 먼 거리만큼을 마지막 이동에서 제외
total_distance -= farthest_distance

print(total_distance)