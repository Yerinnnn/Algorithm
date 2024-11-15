T = int(input())

for test_case in range(1, T + 1):
    # 1주일에 L분 이상, U분 이하의 운동을 해야함
    # 이번 주에 운동한 분 X
    L, U, X = map(int, input().split())
    
    # 운동량 부족 (몇 분 더 운동을 해야 제한을 맞출 수 있는지 출력)
    if X < L:
        result = L - X
    # 운동량 초과 (-1)
    elif X > U:
        result = -1
    # 운동량 적정 (0)
    else:
        result = 0
        
    print(f"#{test_case} {result}")