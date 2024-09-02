from itertools import permutations

def solution(numbers):
    # 모든 숫자 조합 생성
    num_set = set()
    for i in range(1, len(numbers) + 1):
        # permutations()
        # 주어진 iterable에서 가능한 모든 순열(순서가 있는 조합)을 생성
        # 첫 번째 인자: 순열을 만들 대상이 되는 iterable (문자열, 리스트 등)
        # 두 번째 인자: 생성할 순열의 길이 (선택적, 기본값은 iterable의 전체 길이)
        perms = permutations(numbers, i)
        num_set.update(int(''.join(p)) for p in perms)
        
    # 0과 1 제거 (소수가 아님)
    num_set -= set([0, 1])
    
    # 소수 판별
    count = 0
    for num in num_set:
        if is_prime(num):
            count += 1
    return count

def is_prime(n):
    if n < 2:
        return False
    
    # 2부터 √n까지의 수로 나누어 떨어지는지 확인하여 소수를 판별
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True