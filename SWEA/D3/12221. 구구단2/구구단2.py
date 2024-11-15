T = int(input())

for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    result = 0
    
    if A >= 10 or B >= 10:
        result = -1
    else:
        result = A * B
        
    print(f"#{test_case} {result}")