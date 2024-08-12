def max_hamburgers(N, K, line):
    eaten = [False] * N     # 햄버거가 먹혔는지 표시
    count = 0   # 먹을 수 있는 햄버거의 최대 수

    for i in range(N):
        if line[i] == 'P':  # 사람이 있으면
            # i - K : 사람의 위치 i에서 왼쪽으로 K만큼 떨어진 위치
            # (배열의 범위를 벗어날 수 있으므로 0 이상이 되도록 함)
            # i + K : 사람의 위치 i에서 오른쪽으로 K만큼 떨어진 위치 (range의 특성을 고려하여 +1)
            # (배열의 끝을 벗어나지 않도록 N - 1 이하가 되도록 함)
            for j in range(max(0, i - K), min(N, i + K + 1)):
                if line[j] == 'H' and not eaten[j]:
                    eaten[j] = True
                    count += 1
                    break

    return count

# 식탁의 길이 N, 햄버거를 선택할 수 있는 거리 K
N, K = map(int, input().split())
line = input().strip()

# 최대 햄버거 수 출력
print(max_hamburgers(N, K, line))