T = int(input())

for test_case in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())
    
    total_minutes = m1 + m2
    additional_hours = total_minutes // 60
    final_minutes = total_minutes % 60
    
    total_hours = h1 + h2 + additional_hours
    final_hours = total_hours % 12
    if final_hours == 0:
        final_hours = 12
        
    print(f"#{test_case} {final_hours} {final_minutes}")