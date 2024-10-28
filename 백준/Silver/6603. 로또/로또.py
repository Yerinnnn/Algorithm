from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    data = list(map(int, input().split()))
    if data[0] == 0:  # 테스트 케이스 종료 조건
        break
    
    k = data[0]
    numbers = data[1:]
    
    # 6개 숫자를 뽑는 모든 조합 출력
    for comb in combinations(numbers, 6):
        print(" ".join(map(str, comb)))
    
    print()  # 각 테스트 케이스 사이에 빈 줄 추가