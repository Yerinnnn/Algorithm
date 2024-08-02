def find_line_order(N, heights):
    result = [None] * N
    
    for i in range(N):
        taller_count = heights[i]
        count = 0
        for j in range(N):
            if result[j] is None:
                if count == taller_count:
                    result[j] = i + 1
                    break
                count += 1

    return result

N = int(input())
heights = list(map(int, input().split()))

order = find_line_order(N, heights)
print(' '.join(map(str, order)))