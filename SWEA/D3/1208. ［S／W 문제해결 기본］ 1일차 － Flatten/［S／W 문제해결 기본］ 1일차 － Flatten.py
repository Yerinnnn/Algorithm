for test_case in range(1, 11):
    count = int(input())
    boxs = list(map(int, input().split()))
    
    boxs.sort()
    
    for i in range(count):
        boxs[-1] -= 1
        boxs[0] += 1
        boxs.sort()
        
    result = boxs[-1] - boxs[0]
    
    print(f"#{test_case} {result}")