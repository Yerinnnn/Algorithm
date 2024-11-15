T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    result = ""
    
    for i in range(N):
        char, count = input().split()
        count = int(count)
        result += char * count
        
    print(f"#{test_case}")
    for i in range(0, len(result), 10):
        print(result[i:i+10])