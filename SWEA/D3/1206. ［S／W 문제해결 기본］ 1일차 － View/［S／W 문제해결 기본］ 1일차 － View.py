for test_case in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    count = 0
    
    for i in range(2, N-2):
        max_building = max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])
        if buildings[i] > max_building:
            count += buildings[i] - max_building
            
    print(f"#{test_case} {count}")