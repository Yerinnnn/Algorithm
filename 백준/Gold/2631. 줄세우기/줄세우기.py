def length_of_lis(sequence):
    if not sequence:
        return 0

    lis = []  # LIS를 저장할 리스트
    for num in sequence:
        # 현재 숫자가 lis의 가장 큰 값보다 크면 추가
        if not lis or num > lis[-1]:
            lis.append(num)
        else:
            # 이진 탐색을 통해 현재 숫자의 위치 찾기
            left, right = 0, len(lis) - 1
            while left <= right:
                mid = (left + right) // 2
                if lis[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
            # 해당 위치에 num을 대체
            lis[left] = num

    return len(lis)  # LIS의 길이 반환


n = int(input())  # 아이들의 수
sequence = [int(input()) for _ in range(n)]  # 아이들의 현재 순서

lis_length = length_of_lis(sequence)

moves = n - lis_length  # 전체 수에서 LIS의 길이를 뺀 값
print(moves)