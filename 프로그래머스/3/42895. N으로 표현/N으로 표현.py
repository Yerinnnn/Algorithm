def solution(N, number):
    if N == number:
        return 1
    
    # 각 사용 횟수별 가능한 숫자를 저장할 집합 리스트 초기화
    s = [set() for x in range(8)]
    
    # 각 집합에 기본 값 추가
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))
    
    # 1부터 8까지 횟수를 늘려가며 계산
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        
        # 이번 횟수로 만들어진 숫자 중 number가 있는지 확인
        if number in s[i]:
            return i + 1
    
    # 최솟값이 8보다 크면 -1을 return
    return -1