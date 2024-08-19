import sys

# P는 플레이어 수, M은 한 방에 들어갈 수 있는 최대 인원수
P, M = map(int, input().split())

# rooms는 각 방을 저장할 리스트임
# 각 방은 첫 번째 플레이어의 레벨과 해당 방의 플레이어 리스트를 가짐
rooms = []

for _ in range(P):
    level, nickname = input().split() 
    level = int(level)

    placed = False  # 플레이어가 방에 배치되었는지를 나타내는 플래그 변수

    # 이미 존재하는 방에 플레이어를 배치할 수 있는지 확인하는 반복문
    for room in rooms:
        # 방에 자리가 남아 있고, 현재 방의 첫 번째 플레이어와 레벨 차이가 ±10 이내인 경우에만 해당 방에 플레이어를 추가 가능
        if room[0] - 10 <= level <= room[0] + 10 and len(room[1]) < M:
            room[1].append((level, nickname))  # 방의 플레이어 리스트에 현재 플레이어를 추가
            placed = True  # 플레이어가 배치되었음을 표시
            break  # 방에 배치되었으므로 더 이상 다른 방을 확인할 필요가 없으므로 반복문을 종료

    # 기존의 방들 중에서 플레이어를 배치할 수 있는 방이 없을 경우 새로운 방을 생성함
    if not placed:
        # 새로운 방을 생성
        # 방은 첫 번째 플레이어의 레벨과 그 플레이어의 정보를 포함한 리스트로 구성
        rooms.append((level, [(level, nickname)]))

for room in rooms:
    # 방이 꽉 차있으면 "Started!"를 출력함
    if len(room[1]) == M:
        print("Started!")
    else:
        print("Waiting!")
    
    # 방의 플레이어들을 닉네임 기준으로 정렬하여 출력
    for player in sorted(room[1], key=lambda x: x[1]):  # 방의 플레이어들을 닉네임(x[1]) 기준으로 정렬
        print(player[0], player[1])