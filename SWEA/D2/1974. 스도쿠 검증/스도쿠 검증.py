def check(board):
    for i in range(9):
        row_check = set()
        col_check = set()
        box_check = set()
        
        for j in range(9):
            if not (1 <= board[i][j] <= 9) or board[i][j] in row_check:
                return False
            row_check.add(board[i][j])
            
            if not (1 <= board[j][i] <= 9) or board[j][i] in col_check:
                return False
            col_check.add(board[j][i])
            
            box_row = 3 * (i // 3) + j // 3
            box_col = 3 * (i % 3) + j % 3
            if not (1 <= board[box_row][box_col] <= 9) or board[box_row][box_col] in box_check:
                return False
            box_check.add(board[box_row][box_col])
           
    return True

T = int(input())

for test_case in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(9)]
    
    if check(board):
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")