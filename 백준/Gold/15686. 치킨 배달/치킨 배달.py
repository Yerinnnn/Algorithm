from itertools import combinations

# 도시의 치킨 거리를 계산하는 함수
def calculate_city_chicken_distance(houses, selected_chickens):
    total_distance = 0
    for hx, hy in houses:
        # 각 집에서 가장 가까운 치킨집과의 거리 계산
        min_distance = min(abs(hx - cx) + abs(hy - cy) for cx, cy in selected_chickens)
        total_distance += min_distance
    return total_distance

n, m = map(int, input().split())  # n: 도시의 크기, m: 선택할 치킨집 수
city = [list(map(int, input().split())) for _ in range(n)]

houses = []  # 집들의 좌표
chickens = []  # 치킨집들의 좌표

# 도시 정보를 순회하며 집과 치킨집의 좌표를 저장
for r in range(n):
    for c in range(n):
        if city[r][c] == 1:
            houses.append((r, c))
        elif city[r][c] == 2:
            chickens.append((r, c))

# 치킨집 중 M개를 선택하는 모든 조합을 생성
min_city_chicken_distance = float('inf')
for selected_chickens in combinations(chickens, m):
    # 현재 선택된 치킨집들에 대한 도시의 치킨 거리 계산
    city_chicken_distance = calculate_city_chicken_distance(houses, selected_chickens)
    min_city_chicken_distance = min(min_city_chicken_distance, city_chicken_distance)

print(min_city_chicken_distance)