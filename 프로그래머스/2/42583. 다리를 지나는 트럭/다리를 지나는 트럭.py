def solution(bridge_length, weight, truck_weights):
    bridge = [0 for _ in range(bridge_length)]
    current_weight = 0  # 현재 다리 위의 총 무게
    time = 0  # 모든 트럭이 다리를 건너는 데 걸리는 총 시간
    
    # 대기 중인 트럭이 있거나 다리 위에 트럭이 있는 동안 반복
    while truck_weights or current_weight > 0:
        # 매 반복마다 1초씩 증가
        time += 1
        
        # 다리의 맨 앞(가장 먼저 들어간 요소)을 제거하고 그 무게를 현재 무게에서 뺌
        # 트럭이 다리를 완전히 건넌 것을 의미
        current_weight -= bridge.pop(0)
        
        # 대기 중인 트럭이 있고, 다리에 올릴 수 있는 경우
        if truck_weights and current_weight + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)  # 대기열에서 첫 번째 트럭을 가져옴
            bridge.append(truck)  # 다리 맨 뒤에 트럭 추가
            current_weight += truck  # 현재 다리 위 무게 업데이트
        else:
            # 트럭을 올릴 수 없는 경우, 0 추가
            # (다리 길이 유지)
            bridge.append(0)
    
    return time