import sys
from collections import Counter
input = sys.stdin.readline

N, M = map(int, input().split())
words = [input().strip() for _ in range(N)]

# 길이가 M 이상인 단어만 필터링
filtered_words = [word for word in words if len(word) >= M]

# 단어의 빈도수 계산
word_count = Counter(filtered_words)

# 빈도수 높은 순, 길이가 긴 순, 알파벳 순으로 정렬
sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, _ in sorted_words:
    print(word)