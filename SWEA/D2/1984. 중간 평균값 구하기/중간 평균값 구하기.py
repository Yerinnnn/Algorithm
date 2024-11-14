T = int(input())
for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    
    max_num = max(numbers)
    min_num = min(numbers)
    
    total = sum(numbers) - max_num - min_num
    average = round(total / 8)
    
    print(f"#{test_case} {average}")