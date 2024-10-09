def can_install(routers, distance, c):
    count = 1  # 첫 번째 공유기는 항상 설치
    last_installed = routers[0]  # 첫 번째 공유기 설치 위치

    # 각 공유기 위치를 확인
    for i in range(1, len(routers)):
        # 현재 공유기와 이전 설치된 공유기 간의 거리 확인
        if routers[i] - last_installed >= distance:
            count += 1  # 새로운 공유기 설치
            last_installed = routers[i]  # 마지막 설치된 공유기 위치 업데이트

        if count >= c:  # 필요한 수의 공유기를 설치했으면 True 반환
            return True

    return False  # 설치 불가능한 경우


def binary_search(routers, c):
    low = 1  # 최소 거리 초기화
    high = routers[-1] - routers[0]  # 최대 거리 초기화
    answer = 0  # 결과 저장 변수

    while low <= high:
        mid = (low + high) // 2  # 중간 거리 계산
        if can_install(routers, mid, c):  # 중간 거리에서 설치 가능 확인
            answer = mid  # 가능하다면 결과 업데이트
            low = mid + 1  # 더 큰 거리로 탐색
        else:
            high = mid - 1  # 작은 거리로 탐색

    return answer


n, c = map(int, input().split())
routers = [int(input()) for _ in range(n)]

routers.sort()

result = binary_search(routers, c)

print(result)