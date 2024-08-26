def solution(participant, completion):
    # 반환할 정답을 저장할 변수 초기화
    answer = ''

    # 참가자 명단과 완주자 명단을 각각 정렬
    participant.sort()
    completion.sort()

    # 완주자 명단을 순회하면서 각 참가자와 완주자를 비교
    for i in range(len(completion)):
        # 정렬된 리스트에서 동일한 위치의 이름이 일치하지 않는 경우, 해당 참가자가 미완주자
        if participant[i] != completion[i]:
            return participant[i]  # 미완주자를 즉시 반환

    # 만약 모든 참가자와 완주자가 일치하면, 마지막 참가자가 미완주자
    return participant[len(participant) - 1]