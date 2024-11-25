def find_y(x, k):
    result = 0
    bit_position = 0  # X의 비트를 순회하며 0인 비트의 위치를 확인
    k_bit_position = 0  # K의 비트를 순회하며 현재 사용할 비트를 추적

    while k > 0:  # K의 비트가 남아 있는 동안 반복
        # X의 현재 비트가 0인 경우에만 K의 비트를 삽입
        if not (x & (1 << bit_position)):  # X의 bit_position 위치가 0인지 확인
            if k & (1 << k_bit_position):  # K의 현재 비트가 1이면
                result |= (1 << bit_position)  # Y의 해당 위치에 1을 설정
            k >>= 1  # K의 비트를 오른쪽으로 이동 (사용한 비트 삭제)
        bit_position += 1  # X의 다음 비트로 이동

    return result

x, k = map(int, input().split())
print(find_y(x, k))