word = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

for char in word:
    for i in range(len(dial)):
        if char in dial[i]:
            time += i + 3  # 다이얼 번호 2부터 시작하므로 +3
print(time)