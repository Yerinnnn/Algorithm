# 카펫의 가로 길이를 w, 세로 길이를 h라고 할 때:
# w * h = brown + yellow
# (w-2) * (h-2) = yellow (노란색 영역의 크기)
# 2w + 2h - 4 = brown (갈색 영역의 크기)

def solution(brown, yellow):
    total = brown + yellow
    
    for h in range(3, int(total**0.5) + 1):
        if total % h == 0:
            w = total // h
            if (w-2) * (h-2) == yellow:
                return [w, h]