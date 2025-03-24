import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # 데이터 세트 번호, 정수 개수
    k, n = map(int, input().split())
    
    # 한 줄에 최대 10개씩 숫자가 입력 : (n+9)//10 줄을 읽어야 함
    array = []
    for _ in range((n + 9) // 10):
        array.extend(map(int, input().split()))
    
    sorted_array = sorted(array)
    
    # 이동하지 않는 숫자들의 개수 카운트
    # 원래 배열의 숫자가 정렬된 배열의 같은 위치에 있으면 이동하지 않아도 됨
    idx = 0
    for i in range(n):
        if array[i] == sorted_array[idx]:
            idx += 1
    
    # 이동해야 하는 숫자의 개수 = 전체 숫자 개수 - 이동하지 않는 숫자 개수
    moves_needed = n - idx
    
    print(k, moves_needed)