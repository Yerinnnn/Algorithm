T = int(input())
vowels = set('aeiou')

for test_case in range(1, T + 1):
    word = input().strip()
    result = "".join([char for char in word if char not in vowels])
    print(f"#{test_case} {result}")