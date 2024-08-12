from collections import Counter

def count_similar_words(base_word, words):
    base_counter = Counter(base_word)
    similar_count = 0

    for word in words:
        word_counter = Counter(word)
        
        # 준 단어와 각 비교 대상 단어의 문자 빈도를 비교하여 차이를 계산
        difference = sum((base_counter - word_counter).values()) + sum((word_counter - base_counter).values())

        # 비슷한 조건 판별 
        # difference == 0: 두 단어가 완전히 같음
        # difference == 2 and len(base_word) == len(word): 길이가 같고 하나의 문자만 다른 경우
        # difference == 1 and abs(len(base_word) - len(word)) == 1: 두 단어의 길이가 하나 차이나며 한 글자 차이인 경우
        if difference == 0 or (difference == 2 and len(base_word) == len(word)) or (difference == 1 and abs(len(base_word) - len(word)) == 1):
            similar_count += 1

    return similar_count

N = int(input().strip())
base_word = input().strip()
words = [input().strip() for _ in range(N-1)]

# 비슷한 단어의 개수 출력
result = count_similar_words(base_word, words)
print(result)