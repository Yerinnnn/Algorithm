from collections import Counter

def solution(clothes):
    # 의상 종류별로 개수를 카운트
    cloth_counts = Counter([kind for _, kind in clothes])
    
    # 각 종류별로 (의상 개수 + 1)을 곱함
    answer = 1
    for count in cloth_counts.values():
        answer *= (count + 1)
        
    # 아무것도 입지 않는 경우를 제외
    return answer - 1