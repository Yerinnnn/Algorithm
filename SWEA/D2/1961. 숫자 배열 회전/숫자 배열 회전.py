T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [input().split() for _ in range(N)]
    
    # 90도 회전
    rotated_90 = list(zip(*board[::-1]))
    
    # 180도 회전
    rotated_180 = [row[::-1] for row in board[::-1]]
    
    # 270도 회전
    rotated_270 = list(zip(*board))[::-1]
    
    print(f"#{test_case}")
    for i in range(N):
        print("".join(map(str, rotated_90[i])), "".join(map(str, rotated_180[i])), "".join(map(str, rotated_270[i])))