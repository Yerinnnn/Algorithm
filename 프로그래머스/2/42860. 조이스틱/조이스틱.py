def solution(name):
    
    # 알파벳을 만드는 조이스틱 조작 횟수
    def get_change_cost(c):
        return min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)
    
    n = len(name)
    change_cost = sum(get_change_cost(c) for c in name)
    
    # 커서 위치 조이스틱 조작 횟수
    min_move_cost = n - 1
    
    for i in range(n):
        # 오른쪽으로 이동 후 연속된 'A'의 끝을 찾기
        next_index = i + 1
        
        while next_index < n and name[next_index] == 'A':
            next_index += 1
        
        # 이동 거리 계산
        move_cost = i + (n - next_index) + min(i, n - next_index)
        
        min_move_cost = min(min_move_cost, move_cost)
    
    # 문자 변경 비용 + 커서 이동 비용
    return change_cost + min_move_cost