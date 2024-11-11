import sys
input = sys.stdin.readline

# 펜윅 트리 업데이트 함수
def updatefen(i, v):
    while i <= M:
        fen[i] += v
        i += i & -i

# 병사의 위치 찾기 함수
def find(x, i, c):
    # 현재 위치에서 구간 합을 비교하여 병사의 위치를 찾음
    if x <= fen[i] and i <= N and x > fen[i] - data[i]:
        return i
    if x > fen[i]:
        return find(x - fen[i], i + (1 << c), c - 1)
    return find(x, i - (1 << c), c - 1)

# 부대의 개수 N, 명령의 개수 M
N = int(input())
M = 1 << 19
data = [0] + list(map(int, input().split()))

# 펜윅 트리 초기화
fen = [0] * (M + 1)
for i in range(1, N + 1):
    updatefen(i, data[i])

for _ in range(int(input())):
    query = list(map(int, input().split()))
    if query[0] == 1:
        i, v = query[1], query[2]
        updatefen(i, v)
        data[i] += v
    else:
        x = query[1]
        print(find(x, M, 18))