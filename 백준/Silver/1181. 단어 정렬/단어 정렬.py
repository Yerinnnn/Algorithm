N = int(input())
words = set()

for _ in range(N):
    words.add(input().strip())

sorted_words = sorted(words, key=lambda word: (len(word), word))

print('\n'.join(sorted_words))