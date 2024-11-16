def dfs(number, max_swaps, visited):
    global max_value

    # 종료 조건: 남은 교환 횟수가 0일 때
    if max_swaps == 0:
        max_value = max(max_value, int(number))
        return
    
    # 중복 방문 방지
    if (number, max_swaps) in visited:
        return
    visited.add((number, max_swaps))
        
    N = len(number)
    for i in range(N):
        for j in range(i+1, N):
            swapped = list(number)
            swapped[i], swapped[j] = swapped[j], swapped[i]
            dfs("".join(swapped), max_swaps - 1, visited)

T = int(input())

for test_case in range(1, T + 1):
    number, max_swaps = input().split()
    max_swaps = int(max_swaps)
    
    max_value = 0
    visited = set()
    
    dfs(number, max_swaps, visited)
    
    # 교환 후 받을 수 있는 가장 큰 금액
    print(f"#{test_case} {max_value}")