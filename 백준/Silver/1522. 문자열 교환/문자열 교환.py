arr = list(input())
len_arr = len(arr)

# 문자열에서 'a'의 개수를 cnt_a에 저장
cnt_a = arr.count('a')

# 원형 배열처럼 사용하기 위해 배열을 두 배로 늘림
arr = arr + arr

# 결과값을 저장할 변수 res를 큰 값으로 초기화
res = 1000

# 슬라이딩 윈도우 기법을 사용하여 배열의 절반 길이만큼 반복
for i in range(len(arr) // 2):
    # 현재 위치에서 cnt_a만큼의 부분 배열을 선택하고
    # 해당 부분 배열에서 'b'의 개수를 계산
    res = min(res, arr[i:i+cnt_a].count('b'))

# 최소 'b'의 개수를 출력
print(res)