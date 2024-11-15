T = int(input())
for test_case in range(1, T + 1):
    # 격자 크기 N, 파리채 크기 M
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_fliys = float("-inf")
    
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            fliys = sum(board[i+x][j+y] for x in range(M) for y in range(M))
            max_fliys = max(max_fliys, fliys)
            
    print(f"#{test_case} {max_fliys}")