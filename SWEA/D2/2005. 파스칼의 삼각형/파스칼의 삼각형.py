T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    triangle = [[1]]
    
    print(f"#{test_case}")
    print("1")
    
    for i in range(1, N):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
        print(" ".join(map(str, row)))