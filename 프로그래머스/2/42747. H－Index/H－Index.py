def solution(citations):
    # 인용 횟수 리스트를 내림차순으로 정렬
    citations.sort(reverse=True)
    
    # h-index를 찾기 위해 논문의 순위를 순회
    for i in range(len(citations)):
        # i번째 논문의 인용 횟수와 현재 논문의 순위를 비교
        if citations[i] <= i:
            # 논문의 인용 횟수가 순위보다 작거나 같으면
            # 현재까지의 순위가 h-index가 됨
            return i
    
    # 모든 논문의 인용 횟수가 순위보다 크다면
    # 전체 논문의 수가 h-index가 됨
    return len(citations)