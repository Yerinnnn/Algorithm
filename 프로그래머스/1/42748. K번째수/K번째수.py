def solution(array, commands):
    # 결과를 저장할 리스트 초기화
    answer = []
    
    # commands 리스트의 각 명령(command)을 순차적으로 처리
    for i in range(len(commands)):
        # commands[i]는 [i, j, k]의 형태로 주어짐
        # 1. array의 i번째 인덱스부터 j번째 인덱스까지의 부분 배열 추출
        #    이때 인덱스는 1부터 시작하므로 -1을 해줌
        arr = array[commands[i][0]-1:commands[i][1]]
        
        # 2. 추출한 부분 배열을 오름차순으로 정렬
        arr.sort()
        
        # 3. 정렬된 배열에서 k번째 숫자를 결과 리스트에 추가
        #    k는 1부터 시작하므로 -1을 해줌
        answer.append(arr[commands[i][2]-1])
    
    # 모든 명령을 처리한 후 결과 리스트를 반환
    return answer