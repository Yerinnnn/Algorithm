def binary(lst, start, end, M):
    global result
    if start > end:  # 검색 실패
        return
    else:
        mid = (start + end) // 2  # 중앙 원소 고르기
        total = 0  # 예산의 합
        for l in lst:
            if l > mid:
                total += mid
            else:
                total += l
        if total <= M:  # M 이하 이면 중앙값+1 ~ 끝 값 다시 찾기
            result = mid
            return binary(lst, mid + 1, end, M)
        else:
            return binary(lst, start, mid - 1, M)


N = int(input())
lst = list(map(int, input().split()))
M = int(input())
start, end = 1, max(lst)  # 1을 시작, 최댓값을 끝
result = 0  # 출력해야 하는 최대 예산
binary(lst, start, end, M)
print(result)