import sys
input = sys.stdin.readline

# 개강총회를 시작한 시간 start, 개강총회를 끝낸 시간 end, 개강총회 스트리밍을 끝낸 시간 quit_time
start, end, quit_time = input().split()
attendance = set()  # 시작 이후 입장한 사용자 기록
final_count = set()  # 퇴장 기록을 확인한 사용자 기록

# 채팅 기록을 읽어서 조건에 맞는지 검사
while True:
    line = input().strip()
    if not line:
        break
    
    time, user = line.split()
    
    # 시작 시간 이전에 채팅한 사용자는 입장으로 간주
    if time <= start:
        attendance.add(user)
    
    # 퇴장 가능 시간 이후 스트리밍 종료 이전에 채팅한 경우
    if end <= time <= quit_time:
        if user in attendance:  # 입장 기록이 있는 사용자만 퇴장 카운트
            final_count.add(user)

print(len(final_count))