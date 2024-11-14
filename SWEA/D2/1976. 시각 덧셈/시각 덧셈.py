# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''




'''
아래의 구문은 input.txt 를 read only 형식으로 연 후,
앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
아래 구문을 사용하기 위해서는 import sys가 필요합니다.
단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())
    total_hours = 0
    total_minutes = 0
    
    # 이 문제에서는 계산 로직이 복잡하지 않기 때문에 조건문 없이 일관된 방식으로 계산하는 것이 좋음
    # 조건문을 통해 불필요한 연산을 피할 수는 있지만, 현대적인 컴퓨팅 환경에서는 이 정도의 단순 연산 차이는 거의 무시할 수 있는 수준이기 때문에,
    # 복잡성을 줄이고 코드 가독성을 높이는 것이 더 중요할 수 있음
    # 따라서 이 문제의 경우, 조건문 없이 항상 몫과 나머지 연산을 수행하는 것이 가독성과 유지보수 측면에서 더 적합한 선택이라고 판단됨
    
    # total_hours 대신 처음에는 additional_hour라는 이름을 사용하는 것이 
    # 변수의 의미와 역할이 명확하게 드러나기 때문에 가독성을 높일 수 있음
    total_minutes = m1 + m2
    additional_hours = total_minutes // 60
    final_minutes = total_minutes % 60
    
    total_hours = h1 + h2 + additional_hours
    final_hours = total_hours % 12
    # 12시간제에서는 0시 대신 12시로 출력해야 함
    if final_hours == 0:
        final_hours = 12

    print(f"#{test_case} {final_hours} {final_minutes}")