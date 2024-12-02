def is_good_sequence(sequence):
    """
    주어진 수열이 좋은 수열인지 확인.
    인접한 부분 수열이 동일하지 않아야 함.
    """
    length = len(sequence)
    for size in range(1, length // 2 + 1):  # 비교할 부분 수열의 크기
        if sequence[-size:] == sequence[-2 * size:-size]:
            return False
    return True

def backtrack(sequence, n):
    """
    좋은 수열을 구성하는 백트래킹 함수.
    """
    if len(sequence) == n:  # 길이가 N이 되면 출력 후 종료
        print("".join(map(str, sequence)))
        return True

    for num in [1, 2, 3]:  # 1, 2, 3을 순서대로 시도
        sequence.append(num)
        if is_good_sequence(sequence):  # 좋은 수열인지 확인
            if backtrack(sequence, n):  # 유효한 경로 탐색
                return True
        sequence.pop()  # 백트래킹 (수열에서 제거)

    return False

n = int(input())
backtrack([], n)