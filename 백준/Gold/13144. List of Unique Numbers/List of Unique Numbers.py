def count_distinct_subarrays(n: int, arr: list) -> int:
    left = 0  # 왼쪽 포인터
    count = 0  # 서로 다른 부분 배열의 개수
    freq = {}  # 숫자의 빈도를 저장할 딕셔너리

    # 오른쪽 포인터를 통해 배열을 순회
    for right in range(n):
        # 현재 숫자의 빈도 업데이트
        if arr[right] in freq:
            freq[arr[right]] += 1
        else:
            freq[arr[right]] = 1

        # 현재 숫자가 2회 이상 등장하는 동안 왼쪽 포인터를 이동
        while freq[arr[right]] > 1:
            freq[arr[left]] -= 1  # 왼쪽 숫자의 빈도 감소
            if freq[arr[left]] == 0:  # 빈도가 0이 되면 딕셔너리에서 제거
                del freq[arr[left]]
            left += 1  # 왼쪽 포인터 이동

        # 현재 부분 배열의 개수는 right - left + 1
        count += (right - left + 1)

    return count

n = int(input())
arr = list(map(int, input().split()))
result = count_distinct_subarrays(n, arr)
print(result)