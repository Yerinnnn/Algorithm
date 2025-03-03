def solution(sticker):
    # 스티커의 개수가 1개 이하인 경우 예외 처리
    if len(sticker) <= 2:
        return max(sticker)
    
    # 첫 번째 스티커를 무조건 선택하는 경우의 DP
    # 첫 번째 스티커를 선택하면 마지막 스티커는 선택할 수 없음
    dp1 = [0] * len(sticker)
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    
    # 첫 번째 스티커를 선택한 경우의 최대값 계산
    for i in range(2, len(sticker) - 1):
        # 현재 스티커를 선택하거나 선택하지 않는 경우 중 최대값
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
    
    # 첫 번째 스티커를 선택하지 않는 경우의 DP
    dp2 = [0] * len(sticker)
    dp2[1] = sticker[1]
    
    # 첫 번째 스티커를 선택하지 않은 경우의 최대값 계산
    for i in range(2, len(sticker)):
        # 현재 스티커를 선택하거나 선택하지 않는 경우 중 최대값
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
    
    # 두 경우 중 최대값 반환
    # dp1은 마지막 스티커를 선택하지 않았고
    # dp2는 첫 번째와 마지막 스티커를 선택하지 않은 경우의 최대값
    return max(dp1[-2], dp2[-1])