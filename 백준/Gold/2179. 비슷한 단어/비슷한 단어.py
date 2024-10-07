n = int(input())  # 문자열의 개수 입력
a = [input().strip() for _ in range(n)]  # 각 문자열 입력

# 문자열을 인덱스와 함께 사전순으로 정렬
b = sorted(list(enumerate(a)), key=lambda x: x[1])

# 두 문자열의 공통 접두사를 체크하는 함수
def check(str1, str2):
    cnt = 0
    for i in range(min(len(str1), len(str2))):
        if str1[i] == str2[i]:
            cnt += 1
        else:
            break
    return cnt  # 공통 접두사의 길이 반환

# 최장 접두사를 가진 문자열의 길이를 담을 리스트
length = [0] * (n + 1)  # 입력된 문자열의 개수 + 1
maxlength = 0  # 최장 접두사의 길이 초기화

# 인접한 문자열 간의 공통 접두사 길이 확인
for i in range(n - 1):
    # 두 인접한 문자열을 check 함수에 대입
    tmp = check(b[i][1], b[i + 1][1])  # 공통 접두사 길이
    maxlength = max(maxlength, tmp)  # 최장 접두사 길이 갱신

    # 인덱스를 이용하여 length 배열에 저장
    length[b[i][0]] = max(length[b[i][0]], tmp)
    length[b[i + 1][0]] = max(length[b[i + 1][0]], tmp)

first = None  # 최장 접두사를 가진 첫 번째 문자열을 찾기 위한 변수
pre = ""  # 이전 접두사 저장

# 입력된 순서대로 접두사의 길이를 비교
for i in range(n):
    if first is None:  # 첫 번째로 찾는 경우
        if length[i] == max(length):  # 최장 접두사라면
            first = a[i]  # 첫 번째 최장 접두사 문자열
            print(first)  # 결과 출력
            pre = a[i][:maxlength]  # 최장 접두사 저장
    else:  # 이미 첫 번째를 찾은 경우
        if length[i] == max(length) and a[i][:maxlength] == pre:
            print(a[i])  # 동일한 최장 접두사 문자열 출력
            break  # 출력 후 종료