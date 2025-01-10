matrix = [list(map(int, input().split())) for _ in range(9)]
max_value = max(map(max, matrix))

for i in range(9):
    for j in range(9):
        if matrix[i][j] == max_value:
            print(max_value)
            print(i + 1, j + 1)
            break