T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    result = [[0] * N for _ in range(N)]
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction = 0
    
    x, y = 0, 0
    for i in range(1, N * N + 1):
        result[x][y] = i
        dx, dy = directions[direction]
        
        nx, ny = x + dx, y + dy
        
        if nx < 0 or nx >= N or ny < 0 or ny >= N or result[nx][ny] != 0:
            direction = (direction + 1) % 4
            dx, dy = directions[direction]
            nx, ny = x + dx, y + dy
            
        x, y = nx, ny
        
    print(f"#{test_case}")
    for row in result:
        print(" ".join(map(str, row)))