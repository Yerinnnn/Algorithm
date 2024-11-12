T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    digits = set()
    i = 0
    
    while len(digits) < 10:
        i += 1
        current_number = n * i
        digits.update(str(current_number))
        
    print(f"#{test_case} {current_number}")