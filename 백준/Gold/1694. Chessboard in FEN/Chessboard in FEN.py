# 8x8 체스 보드를 구성 (빈 칸은 '.', 기물은 그대로 저장)
def parse_fen(fen):
    board = []
    for row in fen.split('/'):
        board_row = []
        for char in row:
            if char.isdigit():
                board_row.extend(['.'] * int(char))  # 숫자는 빈 칸을 의미
            else:
                board_row.append(char)
        board.append(board_row)
    return board

# 체스 보드 내 유효한 좌표인지 확인
def is_in_bounds(x, y):
    return 0 <= x < 8 and 0 <= y < 8

# 보드의 모든 기물이 공격하는 위치를 계산, attacked 집합에 추가
def mark_attacks(board, attacked):
    directions = {
        'P': [(-1, -1), (-1, 1)],  # 흰색 폰의 공격 방향
        'p': [(1, -1), (1, 1)],    # 검은색 폰의 공격 방향
        'N': [(-2, -1), (-1, -2), (1, -2), (2, -1),
              (2, 1), (1, 2), (-1, 2), (-2, 1)],  # 나이트
        'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],  # 비숍
        'R': [(-1, 0), (1, 0), (0, -1), (0, 1)],    # 룩
        'Q': [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)],  # 퀸
        'K': [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]   # 킹
    }

    for x in range(8):
        for y in range(8):
            piece = board[x][y]
            if piece == '.':
                continue

            if piece in 'Pp':  # 폰은 단순히 한 칸만 공격 가능
                for dx, dy in directions[piece]:
                    nx, ny = x + dx, y + dy
                    if is_in_bounds(nx, ny):
                        attacked.add((nx, ny))
            elif piece in 'NnKk':  # 나이트와 킹은 한 번에 이동
                for dx, dy in directions[piece.upper()]:
                    nx, ny = x + dx, y + dy
                    if is_in_bounds(nx, ny):
                        attacked.add((nx, ny))
            elif piece in 'BbRrQq':  # 비숍, 룩, 퀸은 여러 칸을 이동 가능
                for dx, dy in directions[piece.upper()]:
                    nx, ny = x + dx, y + dy
                    while is_in_bounds(nx, ny):
                        attacked.add((nx, ny))
                        if board[nx][ny] != '.':  # 다른 기물이 있으면 이동 중단
                            break
                        nx, ny = nx + dx, ny + dy

# 공격받지 않은 빈 칸의 개수 계산
def count_safe_squares(board, attacked):
    safe_count = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == '.' and (x, y) not in attacked:
                safe_count += 1
    return safe_count

import sys
input = sys.stdin.read

lines = input().strip().split('\n')
results = []

for fen in lines:
    board = parse_fen(fen)  # FEN 문자열을 8x8 보드로 변환
    attacked = set()        # 공격받는 칸을 저장하는 집합
    mark_attacks(board, attacked)  # 공격받는 칸 계산
    results.append(count_safe_squares(board, attacked))  # 안전한 칸 개수 계산

for result in results:
    print(result)