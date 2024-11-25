import heapq

n = int(input())  # 건물 개수
buildings = []  # 건물 정보

for _ in range(n):
    left, height, right = map(int, input().split())
    # 건물의 시작점, 높이, 끝점 저장
    buildings.append((left, -height, right))  # 시작점: 높이는 음수로 저장 (우선순위 큐를 내림차순 처리)
    buildings.append((right, 0, 0))  # 끝점: 높이를 0으로 처리

events = sorted(buildings)

result = []
active_buildings = [(0, float('inf'))]  # (높이, 끝점)

for x, h, r in events:
    # 시작점인 경우
    if h != 0:
        heapq.heappush(active_buildings, (h, r))  # 높이와 끝점을 우선순위 큐에 추가
    else:
        # 끝점인 경우, 해당 높이를 우선순위 큐에서 제거
        while active_buildings and active_buildings[0][1] <= x:
            heapq.heappop(active_buildings)

    # 현재 가장 높은 건물의 높이를 확인
    max_height = -active_buildings[0][0]

    # 스카이라인 갱신 (높이가 바뀌는 지점만 추가)
    if not result or result[-1][1] != max_height:
        result.append((x, max_height))

for x, h in result:
    print(x, h)