T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))

    max_price = 0
    profit = 0

    # 뒤에서부터 가격을 보면서 최댓값을 업데이트하며 이익 계산
    for price in reversed(prices):
        if price > max_price:
            max_price = price
        else:
            profit += max_price - price

    print(f"#{test_case} {profit}")