import sys

P, M = map(int, input().split())

rooms = []

for _ in range(P):
    level, nickname = input().split()
    level = int(level)

    placed = False
    for room in rooms:
        # 방이 아직 자리가 있고, 레벨 차이가 10 이하이면 그 방에 들어갈 수 있음
        if room[0] - 10 <= level <= room[0] + 10 and len(room[1]) < M:
            room[1].append((level, nickname))
            placed = True
            break

    if not placed:
        # 새로운 방을 생성
        rooms.append((level, [(level, nickname)]))

for room in rooms:
    if len(room[1]) == M:
        print("Started!")
    else:
        print("Waiting!")
    
    # 닉네임 순으로 정렬하여 출력
    for player in sorted(room[1], key=lambda x: x[1]):
        print(player[0], player[1])