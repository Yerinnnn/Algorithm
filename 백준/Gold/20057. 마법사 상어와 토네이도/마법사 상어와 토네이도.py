import sys

n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

# 토네이도의 이동 방향 (좌, 하, 우, 상)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 모래가 퍼지는 비율 배열 정의 (좌측 방향일 때)
# 5x5 배열로 표현, 중앙이 토네이도 위치 (2, 2)
sand_proportion = [
    [0, 0, 0.02, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0.05, 0, 0, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0, 0, 0.02, 0, 0]
]

# 알파 위치 (토네이도 이동 방향에 따른 남은 모래가 이동할 위치)
alpha_positions = [(2, 1), (3, 2), (2, 3), (1, 2)]  # 좌, 하, 우, 상

# 배열을 반시계 방향으로 90도 회전하는 함수
def rotate_90(arr):
    return list(reversed(list(zip(*arr))))

# 각 방향에 대한 모래 비율 배열 계산
proportions = [sand_proportion]
for i in range(3):
    proportions.append(rotate_90(proportions[-1]))

# 토네이도 시뮬레이션 함수
def tornado_simulation():
    # 격자 밖으로 나간 모래의 양
    outside_sand = 0
    
    # 토네이도 시작 위치 (격자 중앙)
    x, y = n // 2, n // 2
    
    # 현재 방향 (0: 좌, 1: 하, 2: 우, 3: 상)
    direction = 0
    
    # 토네이도가 한 방향으로 이동할 거리
    distance = 1
    
    # 현재까지 이동한 거리
    moved = 0
    
    # 현재 사용할 모래 비율 배열
    proportion = proportions[direction]
    
    # 토네이도가 (0,0)에 도달할 때까지 반복
    while not (x == 0 and y == 0):
        # 현재 방향으로 이동
        x += dx[direction]
        y += dy[direction]
        moved += 1
        
        # 현재 위치의 모래 양
        sand = grid[x][y]
        grid[x][y] = 0  # 현재 위치의 모래 제거
        
        # 남은 모래 (알파 위치로 이동할 모래)
        left_sand = sand
        
        # 비율에 따라 모래 분산
        for r in range(5):
            for c in range(5):
                # 현재 위치에서 비율에 해당하는 모래 양
                now_sand = int(sand * proportion[r][c])
                left_sand -= now_sand
                
                # 모래가 이동할 새 위치
                nx, ny = x + r - 2, y + c - 2
                
                # 격자 내부인 경우
                if 0 <= nx < n and 0 <= ny < n:
                    grid[nx][ny] += now_sand
                else:
                    outside_sand += now_sand
        
        # 알파 위치에 남은 모래 이동
        alpha_r, alpha_c = alpha_positions[direction]
        nx, ny = x + alpha_r - 2, y + alpha_c - 2
        
        if 0 <= nx < n and 0 <= ny < n:
            grid[nx][ny] += left_sand
        else:
            outside_sand += left_sand
        
        # 방향 전환 및 이동 거리 조정
        if moved == distance // 2 or moved == distance:
            direction = (direction + 1) % 4
            proportion = proportions[direction]
            
            # 이동 거리 조정
            if moved == distance:
                moved = 0
                distance += 2
    
    return outside_sand

print(tornado_simulation())