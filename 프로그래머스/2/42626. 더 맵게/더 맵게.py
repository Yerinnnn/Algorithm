import heapq

def solution(scoville, K):
    # 이제 scoville[0]이 항상 가장 낮은 스코빌 지수
    heapq.heapify(scoville)
    mix_count = 0
    
    # 힙의 크기가 2 미만이 될 때까지 계속
    # (더 이상 섞을 수 있는 음식이 없을 때까지)
    while len(scoville) >= 2:
        if scoville[0] >= K:
            return mix_count
        
        # 가장 낮은 두 개의 스코빌 지수를 추출
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        # 새로운 스코빌 지수를 계산
        new_scoville = first + (second * 2)
        
        heapq.heappush(scoville, new_scoville)
        
        mix_count += 1
        
    if scoville[0] >= K:
        return mix_count
    
    return -1