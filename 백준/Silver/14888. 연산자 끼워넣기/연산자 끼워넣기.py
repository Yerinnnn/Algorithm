from itertools import permutations

N = int(input())
numbers = list(map(int, input().split()))
# 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수
count = list(map(int, input().split()))
operators = []
for op, cnt in zip(['+', '-', '*', '/'], count):
    operators.extend([op] * cnt)

max_result = float('-inf')
min_result = float('inf')

def calculate(nums, ops):
    result = nums[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            result += nums[i + 1]
        elif ops[i] == '-':
            result -= nums[i + 1]
        elif ops[i] == '*':
            result *= nums[i + 1]
        else:  # 나눗셈
            if result < 0:
                result = -(-result // nums[i + 1])
            else:
                result = result // nums[i + 1]
    return result

for ops in set(permutations(operators)):  # 순열을 만들고 set으로 중복 제거
    current = calculate(numbers, ops)
    max_result = max(max_result, current)
    min_result = min(min_result, current)

print(max_result)
print(min_result)