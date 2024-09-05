from itertools import product

def solution(word):
    letters = ["A", "E", 'I', 'O', 'U']
    dictionary = []
    
    for i in range(1, 6):
        dictionary.extend(list(''.join(words) for words in list(product(letters, repeat=i))))
    
    dictionary.sort()
    
    return dictionary.index(word) + 1