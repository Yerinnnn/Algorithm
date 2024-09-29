n = int(input())
arr = list(map(int, input().split()))
arr.sort()

count = 0

for i in range(n):
    target = arr[i]  # i번째 원소가 좋은 수인지 확인
    left = 0
    right = n - 1
    
    # 투 포인터로 두 수의 합을 찾아 검사
    while left < right:
        if left == i:  # target과 같은 인덱스는 건너뜀
            left += 1
            continue
        if right == i:  # target과 같은 인덱스는 건너뜀
            right -= 1
            continue

        total = arr[left] + arr[right]
        
        if total == target:  # 두 수의 합이 target과 같으면
            count += 1
            break  # 한 번 찾으면 더 확인할 필요 없음
        elif total < target:  # 두 수의 합이 target보다 작으면
            left += 1
        else:  # 두 수의 합이 target보다 크면
            right -= 1

print(count)