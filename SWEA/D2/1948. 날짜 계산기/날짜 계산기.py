days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())

for test_case in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())
    result = 0
    
    if m1 == m2:
        result = d2 - d1 + 1
    else:
        result = days_in_month[m1] - d1 + 1
        result += sum(days_in_month[month] for month in range(m1 + 1, m2))
        result += d2
    
    # 두 번째 날짜가 첫 번째 날짜의 며칠째인지 출력
    print(f"#{test_case} {result}")