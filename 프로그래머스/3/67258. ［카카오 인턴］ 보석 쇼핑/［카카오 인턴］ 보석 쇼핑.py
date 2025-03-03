def solution(gems):
    # 모든 보석의 종류 집합 생성
    gem_types = set(gems)
    
    # 전체 보석 종류의 개수
    total_types = len(gem_types)
    
    # 결과 변수 초기화 (구간의 시작, 끝, 길이)
    answer = [0, len(gems) - 1]
    min_length = len(gems)
    
    # 투 포인터 알고리즘에 사용할 변수들
    start = 0
    current_gems = {}
    
    # 포인터를 오른쪽으로 이동하며 탐색
    for end in range(len(gems)):
        # 현재 보석 추가
        current_gems[gems[end]] = current_gems.get(gems[end], 0) + 1
        
        # 모든 보석 종류를 포함했을 때
        while len(current_gems) == total_types:
            # 현재 구간 길이 계산
            current_length = end - start
            
            # 최소 길이 구간 업데이트
            if current_length < min_length:
                min_length = current_length
                answer = [start, end]
            
            # 시작 포인터의 보석 제거
            current_gems[gems[start]] -= 1
            
            # 해당 보석의 개수가 0이 되면 딕셔너리에서 제거
            if current_gems[gems[start]] == 0:
                del current_gems[gems[start]]
            
            # 시작 포인터 이동
            start += 1
    
    # 인덱스는 1부터 시작하므로 1 더하기
    return [answer[0] + 1, answer[1] + 1]