from itertools import permutations

def solution(k, dungeons):
    max_dungeons = 0
    
    # 모든 던전 탐험 순서를 고려하기 위해 순열을 생성
    for perm in permutations(dungeons, len(dungeons)):
        current_fatigue = k  # 현재 피로도
        cleared_dungeons = 0  # 탐험한 던전 수 초기화
        
        for required, consume in perm:
            # 현재 피로도가 던전의 최소 필요 피로도 이상인 경우, 탐험 가능
            if current_fatigue >= required:
                current_fatigue -= consume  # 던전을 탐험하고 피로도 소모
                cleared_dungeons += 1  # 탐험한 던전 수 증가
            else:
                break
                
        # 탐험한 던전 수의 최댓값 갱신
        max_dungeons = max(max_dungeons, cleared_dungeons)
        
    return max_dungeons