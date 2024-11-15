T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    incomes = list(map(int, input().split()))
    
    average = sum(incomes) / N
    below_average_count = sum(1 for income in incomes if income <= average)
    
    # 평균 이하의 소득을 가진 사람들의 수
    print(f"#{test_case} {below_average_count}")