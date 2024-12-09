def can_travel(line, L):
    n = len(line)
    used = [False] * n  # 경사로 설치 여부 기록

    for i in range(n - 1):
        if line[i] == line[i + 1]:  # 높이가 같으면 계속 진행
            continue
        elif line[i] + 1 == line[i + 1]:  # 올라가는 경사로 설치
            for j in range(i, i - L, -1):  # 이전 L칸 확인
                if j < 0 or line[j] != line[i] or used[j]:
                    return False
                used[j] = True
        elif line[i] - 1 == line[i + 1]:  # 내려가는 경사로 설치
            for j in range(i + 1, i + L + 1):  # 이후 L칸 확인
                if j >= n or line[j] != line[i + 1] or used[j]:
                    return False
                used[j] = True
        else:  # 높이 차이가 1보다 크면 이동 불가능
            return False
    return True

n, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

result = 0

# 행 검사
for row in grid:
    if can_travel(row, L):
        result += 1

# 열 검사
for col in zip(*grid):  # 열을 추출 (전치 행렬)
    if can_travel(col, L):
        result += 1

print(result)