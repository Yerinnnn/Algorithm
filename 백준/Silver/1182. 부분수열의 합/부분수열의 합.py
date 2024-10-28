n, s = map(int, input().split())
arr = list(map(int, input().split()))

# 부분 집합의 합이 S가 되는 경우의 수 초기화
count = 0

def backtrack(index, current_sum):
    global count

    # 모든 요소를 탐색한 경우
    if index == n:
        # 부분 집합의 합이 S와 같을 때 카운트 증가
        if current_sum == s:
            count += 1
        return
    
    # 현재 요소를 포함하는 경우와 포함하지 않는 경우로 분기
    backtrack(index + 1, current_sum + arr[index])  # 현재 요소 포함
    backtrack(index + 1, current_sum)               # 현재 요소 미포함

backtrack(0, 0)

# 공집합 제외 (S가 0인 경우)
if s == 0:
    count -= 1

print(count)