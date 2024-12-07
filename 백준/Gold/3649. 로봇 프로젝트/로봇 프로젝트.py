import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input())  # 구멍의 너비 (단위: cm)
        n = int(input())  # 레고 블록의 개수
        blocks = [int(input()) for _ in range(n)]  # 레고 블록 길이 리스트

        target = x * 10**7  # 목표 길이 (나노미터 단위)
        blocks.sort()  # 레고 블록 길이를 정렬

        # 투 포인터 설정
        left, right = 0, n - 1
        found = False
        result = (0, 0)  # 선택된 두 블록의 길이 저장

        while left < right:
            current_sum = blocks[left] + blocks[right]
            if current_sum == target:
                # 두 블록의 길이를 기록
                result = (blocks[left], blocks[right])
                found = True
                break
            elif current_sum < target:
                left += 1  # 합이 부족하면 왼쪽 포인터를 이동
            else:
                right -= 1  # 합이 넘치면 오른쪽 포인터를 이동

        if found:
            print(f"yes {result[0]} {result[1]}")
        else:
            print("danger")
    except:
        break  # 입력이 끝나면 종료