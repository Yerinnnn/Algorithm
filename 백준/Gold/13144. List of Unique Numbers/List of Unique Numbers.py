import sys

def count_unique_subarrays(N, A):
    seen = set()  # 현재 부분 수열 내의 숫자 집합
    count = 0     # 중복 없는 부분 수열 개수
    R = 0         # 오른쪽 포인터

    for L in range(N):  # L을 0부터 N-1까지 이동
        while R < N and A[R] not in seen:
            seen.add(A[R])  # 새로운 원소 추가
            R += 1  # 오른쪽 확장

        count += (R - L)  # 가능한 부분 수열 개수 추가
        seen.remove(A[L])  # L을 이동하며 숫자 제거

    return count

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))

print(count_unique_subarrays(N, A))