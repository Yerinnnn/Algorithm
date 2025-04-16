numbers = sorted(int(input()) for _ in range(5))

average = sum(numbers) // 5
median = numbers[2]

print(average)
print(median)