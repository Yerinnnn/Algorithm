numbers = [int(input()) for _ in range(9)]
max_num = max(numbers)
print(max_num)
print(numbers.index(max_num) + 1)