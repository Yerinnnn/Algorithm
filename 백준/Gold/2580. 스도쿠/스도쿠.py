import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
blanks = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

# 사용 여부 기록 (행, 열, 박스 별 숫자 사용 여부)
row = [[False]*10 for _ in range(9)]
col = [[False]*10 for _ in range(9)]
square = [[False]*10 for _ in range(9)]

# 초기 상태 반영
for i in range(9):
    for j in range(9):
        num = board[i][j]
        if num != 0:
            row[i][num] = True
            col[j][num] = True
            square[(i//3)*3 + j//3][num] = True

def solve(idx):
    if idx == len(blanks):
        for r in board:
            print(*r)
        sys.exit()  # 정답 찾으면 바로 종료

    x, y = blanks[idx]
    s = (x//3)*3 + y//3  # 3x3 박스 번호

    for num in range(1, 10):
        if not row[x][num] and not col[y][num] and not square[s][num]:
            board[x][y] = num
            row[x][num] = col[y][num] = square[s][num] = True
            solve(idx + 1)
            board[x][y] = 0
            row[x][num] = col[y][num] = square[s][num] = False

solve(0)