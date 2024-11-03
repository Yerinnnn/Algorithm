N = int(input())
room = [input() for _ in range(N)]

# 가로 방향 자리 수 찾기
horizontal_count = 0
for row in room:
    count = 0
    for char in row:
        if char == '.':
            count += 1
        else:
            if count >= 2:
                horizontal_count += 1
            count = 0
    if count >= 2:
        horizontal_count += 1

# 세로 방향 자리 수 찾기
vertical_count = 0
for col in range(N):
    count = 0
    for row in range(N):
        if room[row][col] == '.':
            count += 1
        else:
            if count >= 2:
                vertical_count += 1
            count = 0
    if count >= 2:
        vertical_count += 1

print(horizontal_count, vertical_count)