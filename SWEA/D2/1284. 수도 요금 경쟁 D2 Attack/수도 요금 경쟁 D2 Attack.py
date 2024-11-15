T = int(input())

for test_case in range(1, T + 1):
    # A사 : 1리터당 P원
    # B사 : 기본 요금이 Q원, 월간 사용량이 R리터 이하인 경우 기본 요금, 초과할 경우 초과량에 대해 1리터당 S원의 요금
    # 한 달간 사용하는 수도의 양 W
    P, Q, R, S, W = map(int, input().split())
    
    a_price = W * P
    b_price = Q if W <= R else Q + (W - R) * S
    result = min(a_price, b_price)
    
    # 요금이 더 저렴한 회사를 골라 그 요금을 출력
    print(f"#{test_case} {result}")