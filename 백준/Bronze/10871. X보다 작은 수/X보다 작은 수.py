N, X = map(int, input().split())
numbers = list(map(int, input().split()))
print(*[num for num in numbers if num < X])