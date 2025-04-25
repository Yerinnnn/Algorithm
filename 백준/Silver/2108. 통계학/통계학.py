import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

# 산술평균
avg = round(sum(nums) / N)

# 중앙값
nums.sort()
median = nums[N // 2]

# 최빈값
count = Counter(nums)
freq = count.most_common()  # [(값, 빈도), ...] 형태로 정렬
max_freq = freq[0][1]

# 최빈값이 여러 개일 경우 처리
modes = [num for num, cnt in freq if cnt == max_freq]
modes.sort()
mode = modes[1] if len(modes) > 1 else modes[0]

# 범위
range_ = nums[-1] - nums[0]

# 결과 출력
print(avg)
print(median)
print(mode)
print(range_)