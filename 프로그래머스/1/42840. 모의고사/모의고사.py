def solution(answers):
    # 수포자 1, 2, 3의 답안 패턴을 리스트로 정의
    student1 = [1, 2, 3, 4, 5]  # 5개의 패턴 반복
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 8개의 패턴 반복
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10개의 패턴 반복
    
    # 각 학생의 점수를 저장할 리스트 초기화
    scores = [0, 0, 0]
    
    # 제출된 답안을 순회하며 각 학생의 점수를 계산
    for i in range(len(answers)):
        # i번째 문제에 대해 각 학생의 패턴과 비교하여 점수를 증가시킴
        if answers[i] == student1[i % len(student1)]:
            scores[0] += 1
        if answers[i] == student2[i % len(student2)]:
            scores[1] += 1
        if answers[i] == student3[i % len(student3)]:
            scores[2] += 1
    
    # 가장 높은 점수를 찾음
    max_score = max(scores)
    
    # 가장 높은 점수를 받은 학생들의 번호를 리스트로 반환
    result = []
    for i in range(3):
        if scores[i] == max_score:
            result.append(i + 1)
    
    return result

# 테스트 실행 예시
# 예를 들어, answers = [1,2,3,4,5] 이면, 수포자1이 모든 문제를 맞춰 가장 높은 점수를 받음
print(solution([1, 2, 3, 4, 5]))  # 결과: [1]