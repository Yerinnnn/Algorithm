T = int(input())
units = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for test_case in range(1, T + 1):
    N = int(input())
    result = []
    count = 0
    
    for unit in units:
        count = N // unit
        result.append(count)
        N %= unit
        
    print(f"#{test_case}")
    print(" ".join(map(str, result)))