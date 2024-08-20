from collections import defaultdict

def max_length_with_limit(arr, K):
    count = defaultdict(int)  # 각 숫자의 등장 횟수를 기록할 딕셔너리, 기본값이 0인 defaultdict로 초기화
    max_length = 0  # 최대 부분 배열 길이를 저장할 변수, 초기값은 0
    left = 0  # 슬라이딩 윈도우의 왼쪽 끝을 가리키는 포인터, 초기값은 0

    # 슬라이딩 윈도우를 이용하여 배열의 각 요소를 순차적으로 처리
    for right in range(len(arr)):
        count[arr[right]] += 1  # 현재 숫자의 등장 횟수를 증가시킴
        
        # 특정 숫자의 등장 횟수가 K를 초과하는 경우, 조건을 만족시킬 때까지 윈도우의 왼쪽 끝을 이동
        while count[arr[right]] > K:
            count[arr[left]] -= 1  # 왼쪽 끝 숫자의 등장 횟수를 감소
            left += 1  # 윈도우의 왼쪽 끝을 오른쪽으로 한 칸 이동

        # 현재 윈도우의 길이 계산 및 최대 길이 갱신
        max_length = max(max_length, right - left + 1)

    return max_length  # 조건을 만족하는 가장 긴 부분 배열의 길이를 반환

# 배열의 크기 N과 특정 숫자의 최대 허용 등장 횟수 K
N, K = map(int, input().split())

arr = list(map(int, input().split()))

print(max_length_with_limit(arr, K))