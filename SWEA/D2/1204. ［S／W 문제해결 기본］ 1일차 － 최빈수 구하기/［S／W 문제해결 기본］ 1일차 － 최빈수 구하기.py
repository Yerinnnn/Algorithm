from collections import Counter

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    
    frequency = Counter(numbers)
    
    max_frequency = max(frequency.values())
    mode_score = max(score for score, count in frequency.items() if count == max_frequency)
    
    print(f"#{test_case} {mode_score}")