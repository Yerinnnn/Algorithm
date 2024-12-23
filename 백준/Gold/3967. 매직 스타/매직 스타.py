# 매직 스타의 모양 입력
star = [list(input().strip()) for _ in range(5)]

# 빈칸과 숫자 관리
positions = []  # 빈칸의 좌표
used = [False] * 13  # 숫자 1~12 사용 여부
lines = [
    [(0, 4), (1, 3), (2, 2), (3, 1)],  # 첫 번째 직선
    [(0, 4), (1, 5), (2, 6), (3, 7)],  # 두 번째 직선
    [(1, 1), (1, 3), (1, 5), (1, 7)],  # 세 번째 직선
    [(3, 1), (3, 3), (3, 5), (3, 7)],  # 네 번째 직선
    [(1, 1), (2, 2), (3, 3), (4, 4)],  # 다섯 번째 직선
    [(1, 7), (2, 6), (3, 5), (4, 4)]   # 여섯 번째 직선
]

# 빈칸 좌표 수집
for i in range(5):
    for j in range(9):
        if star[i][j] == 'x':
            positions.append((i, j))
        elif star[i][j].isalpha():
            used[ord(star[i][j]) - ord('A') + 1] = True  # 이미 배치된 숫자

# 직선 합 계산
def calculate_line_sum(line):
    total = 0
    for x, y in line:
        if star[x][y] == 'x':  # 빈칸이면 계산 불가
            return None
        total += ord(star[x][y]) - ord('A') + 1
    return total

# 백트래킹 함수
def solve(index):
    if index == len(positions):  # 모든 빈칸을 채웠다면
        for line in lines:
            total = calculate_line_sum(line)
            if total is not None and total != 26:
                return
        for row in star:
            print("".join(row))
        exit(0)

    x, y = positions[index]
    for num in range(1, 13):
        if not used[num]:  # 사용하지 않은 숫자만 배치
            star[x][y] = chr(num + ord('A') - 1)
            used[num] = True

            # 가지치기: 현재 배치가 유효한지 확인
            is_valid = True
            for line in lines:
                if (x, y) in line:
                    total = calculate_line_sum(line)
                    if total is not None and total > 26:
                        is_valid = False
                        break

            if is_valid:
                solve(index + 1)

            # 상태 복구
            used[num] = False
            star[x][y] = 'x'

solve(0)