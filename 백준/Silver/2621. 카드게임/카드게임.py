from collections import Counter

cards = [input().split() for _ in range(5)]
colors = [card[0] for card in cards]
numbers = sorted(int(card[1]) for card in cards)

# 색깔과 숫자 빈도수 계산
color_count = Counter(colors)
number_count = Counter(numbers)

# 점수 계산을 위한 조건 확인
max_color_count = max(color_count.values())
max_number_count = max(number_count.values())
unique_numbers = len(number_count)
is_straight = all(numbers[i] + 1 == numbers[i + 1] for i in range(4))

score = 0

# 1. 같은 색깔 5장 + 연속된 숫자 (Straight Flush)
if max_color_count == 5 and is_straight:
    score = 900 + numbers[-1]

# 2. 같은 숫자 4장 (Four of a Kind)
elif max_number_count == 4:
    for num, count in number_count.items():
        if count == 4:
            score = 800 + num
            break

# 3. 3장 같은 숫자 + 2장 같은 숫자
elif max_number_count == 3 and unique_numbers == 2:
    three_num = max(k for k, v in number_count.items() if v == 3)
    two_num = max(k for k, v in number_count.items() if v == 2)
    score = 700 + three_num * 10 + two_num

# 4. 같은 색깔 5장
elif max_color_count == 5:
    score = 600 + numbers[-1]

# 5. 연속된 숫자 5장
elif is_straight:
    score = 500 + numbers[-1]

# 6. 같은 숫자 3장
elif max_number_count == 3:
    for num, count in number_count.items():
        if count == 3:
            score = 400 + num
            break

# 7. 2장 같은 숫자 두 개
elif list(number_count.values()).count(2) == 2:
    pairs = sorted([k for k, v in number_count.items() if v == 2], reverse=True)
    single = [k for k, v in number_count.items() if v == 1][0]
    score = 300 + pairs[0] * 10 + pairs[1]

# 8. 2장 같은 숫자 한 개
elif max_number_count == 2:
    pair = max(k for k, v in number_count.items() if v == 2)
    score = 200 + pair

# 9. 그 외
else:
    score = 100 + numbers[-1]

print(score)