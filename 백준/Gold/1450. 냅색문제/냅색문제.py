import sys
from itertools import combinations
from bisect import bisect_right

input = sys.stdin.readline

N, C = map(int, input().split())  # 물건 개수, 무게 제한
weights = list(map(int, input().split()))  # 각 물건의 무게

# 배열을 두 부분으로 나누기
mid = N // 2
left = weights[:mid]  # 왼쪽 절반
right = weights[mid:]  # 오른쪽 절반

# 부분 집합의 합을 계산하는 함수
def get_subset_sums(array):
    subset_sums = []
    for r in range(len(array) + 1):
        for comb in combinations(array, r):
            subset_sums.append(sum(comb))
    return subset_sums

# 왼쪽과 오른쪽 부분 집합의 합 계산
left_sums = get_subset_sums(left)
right_sums = get_subset_sums(right)

# 오른쪽 부분 집합의 합을 정렬 (이분 탐색을 위해)
right_sums.sort()

# 가능한 부분 집합의 합 계산
result = 0
for left_sum in left_sums:
    # 오른쪽 합과 더했을 때 C 이하가 되는 개수 계산
    remaining_capacity = C - left_sum
    if remaining_capacity >= 0:
        result += bisect_right(right_sums, remaining_capacity)

print(result)