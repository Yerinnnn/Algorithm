def remove_explosive_string(s: str, bomb: str) -> str:
    stack = []  # 결과 문자열 스택
    
    # 입력 문자열의 각 문자를 순회
    for char in s:
        stack.append(char)  # 현재 문자를 스택에 추가
        
        # 스택의 마지막 부분이 폭발 문자열과 일치하는지 확인
        if ''.join(stack[-len(bomb):]) == bomb:
            # 일치할 경우, 스택의 마지막 len(bomb) 개 문자를 제거
            del stack[-len(bomb):]

    # 스택을 합쳐서 최종 결과 문자열 생성
    result = ''.join(stack)
    
    # 결과가 비어있다면 'FRULA' 반환
    return result if result else 'FRULA'

s = input()
bomb = input()
result = remove_explosive_string(s, bomb)
print(result)