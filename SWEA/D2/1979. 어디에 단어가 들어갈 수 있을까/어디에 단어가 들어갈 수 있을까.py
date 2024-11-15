def check(puzzle, K):
    result = 0
    # cell == 0 일 경우,
    # if count == K: result += 1, count = 0
    # 하나의 row가 끝났을 때,
    # if count == K: result += 1, count = 0
    for row in puzzle:
        count = 0
        for cell in row:
            # cell이 흰색일 경우
            if cell == 1:
                count += 1
            else:
            # cell이 검은색일 경우
                if count == K: 
                    result += 1
                count = 0
        # # 하나의 row가 끝났을 때
        if count == K: 
            result += 1
    return result

T = int(input())

for test_case in range(1, T + 1):
    # 퍼즐의 가로, 세로 길이 N, 단어의 길이 K
    N, K = map(int, input().split())
    # 흰색 부분은 1, 검은색 부분은 0 
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    
    total_result = check(puzzle, K)  # 가로 방향 탐색
    total_result += check(list(zip(*puzzle)), K)  # 세로 방향 탐색
                
    # 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력
    print(f"#{test_case} {total_result}")