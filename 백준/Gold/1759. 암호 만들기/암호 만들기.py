from itertools import combinations

# 암호의 길이 L, 사용할 수 있는 알파벳의 개수 C, 알파벳 리스트
L, C = map(int, input().split())
letters = input().split()

# 알파벳을 사전순으로 정렬 (출력 조건)
letters.sort()

# 모음 리스트
vowels = {'a', 'e', 'i', 'o', 'u'}

# 조건에 맞는 암호 조합 출력
for comb in combinations(letters, L):  # letters 중 L개의 알파벳을 선택하는 모든 조합
    num_vowels = sum(1 for char in comb if char in vowels)  # 조합 내 모음의 개수 계산
    num_consonants = L - num_vowels  # 자음의 개수는 전체 길이에서 모음의 개수를 뺀 값
    
    # 최소 한 개의 모음과 최소 두 개의 자음으로 구성된 경우 출력
    if num_vowels >= 1 and num_consonants >= 2:
        print(''.join(comb))  # 조합을 문자열로 변환하여 출력