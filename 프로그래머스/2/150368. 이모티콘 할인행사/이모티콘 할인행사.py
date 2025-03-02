from itertools import product

def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]  # 가능한 할인율
    best_result = [0, 0]  # [최대 가입자 수, 최대 판매액]

    # 1. 가능한 모든 할인율 조합 생성
    for discounts in product(discount_rates, repeat=len(emoticons)):
        subscribers, total_sales = 0, 0  # 현재 할인율 조합에서의 결과

        # 2. 각 사용자별 구매 계산
        for min_discount, subscribe_threshold in users:
            user_total = 0  # 사용자의 총 구매 금액

            # 3. 사용자가 원하는 할인율 이상인 이모티콘만 구매
            for emoticon_price, discount in zip(emoticons, discounts):
                if discount >= min_discount:  # 원하는 할인율 이상이면 구매
                    user_total += emoticon_price * (100 - discount) // 100

            # 4. 사용자의 구매액이 기준을 넘으면 플러스 가입
            if user_total >= subscribe_threshold:
                subscribers += 1
            else:
                total_sales += user_total  # 아니면 판매액에 추가

        # 5. 결과 갱신 (가입자 수가 많거나, 같을 경우 판매액이 크면 갱신)
        if subscribers > best_result[0] or (subscribers == best_result[0] and total_sales > best_result[1]):
            best_result = [subscribers, total_sales]

    return best_result