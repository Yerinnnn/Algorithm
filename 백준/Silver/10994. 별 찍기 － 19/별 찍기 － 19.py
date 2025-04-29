def fill(x, y, length):
    if length == 1:
        stars[x][y] = '*'
        return

    # 맨 윗줄과 아랫줄
    for i in range(length):
        stars[x][y + i] = '*'
        stars[x + length - 1][y + i] = '*'

    # 맨 왼쪽줄과 오른쪽줄
    for i in range(1, length - 1):
        stars[x + i][y] = '*'
        stars[x + i][y + length - 1] = '*'

    fill(x + 2, y + 2, length - 4)


n = int(input())
size = 4 * (n - 1) + 1
stars = [[' ' for _ in range(size)] for _ in range(size)]

fill(0, 0, size)

for row in stars:
    print(''.join(row))