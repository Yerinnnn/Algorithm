T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    
    numbers.sort()
    
    print(f"#{test_case}", " ".join(map(str, numbers)))