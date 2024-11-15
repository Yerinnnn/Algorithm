T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    digits = set()
    i = 0
    
    while len(digits) < 10:
        i += 1
        current_number = N * i
        digits.update(str(current_number))
    
    print(f"#{test_case} {current_number}")