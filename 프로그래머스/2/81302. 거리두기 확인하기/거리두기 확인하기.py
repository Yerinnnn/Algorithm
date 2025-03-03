def solution(places):
    def check_distance(room):
        # 대기실 전체를 순회하며 응시자(P) 위치 찾기
        for r in range(5):
            for c in range(5):
                if room[r][c] == 'P':
                    # 해당 응시자 주변 거리두기 확인
                    if not is_safe_position(room, r, c):
                        return 0
        return 1
    
    def is_safe_position(room, r, c):
        # 4방향 탐색을 위한 방향 벡터 (상, 하, 좌, 우)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # 1. 상하좌우 바로 옆 자리 확인 (맨해튼 거리 1)
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 5 and 0 <= nc < 5:
                if room[nr][nc] == 'P':
                    return False
        
        # 2. 대각선 방향 확인 (맨해튼 거리 2)
        diagonals = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dr, dc in diagonals:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 5 and 0 <= nc < 5:
                if room[nr][nc] == 'P':
                    # 대각선에 응시자가 있다면, 중간에 파티션이 없는지 확인
                    mid_r, mid_c = r + dr, c
                    mid2_r, mid2_c = r, c + dc
                    if room[mid_r][mid_c] != 'X' or room[mid2_r][mid2_c] != 'X':
                        return False
        
        # 3. 맨해튼 거리 2인 상하좌우 확인
        distance_two = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        for dr, dc in distance_two:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 5 and 0 <= nc < 5:
                if room[nr][nc] == 'P':
                    # 중간에 파티션이 없는지 확인
                    mid_r, mid_c = r + dr//2, c + dc//2
                    if room[mid_r][mid_c] != 'X':
                        return False
        
        return True
    
    # 각 대기실에 대해 거리두기 준수 여부 확인
    return [check_distance(room) for room in places]