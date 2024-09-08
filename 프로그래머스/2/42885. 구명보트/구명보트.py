def solution(people, limit):
    people.sort()  # 몸무게를 오름차순으로 정렬
    left = 0       # 가장 가벼운 승객의 인덱스
    right = len(people) - 1  # 가장 무거운 승객의 인덱스
    boats = 0      # 필요한 보트의 수

    while left <= right:
        # 현재 가장 가벼운 승객과 가장 무거운 승객의 몸무게 합이 limit 이하이면
        if people[left] + people[right] <= limit:
            left += 1  # 가장 가벼운 승객 탑승
        right -= 1  # 가장 무거운 승객 탑승
        boats += 1  # 보트의 수를 증가

    return boats  # 필요한 보트의 수를 반환