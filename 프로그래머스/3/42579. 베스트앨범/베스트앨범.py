def solution(genres, plays):
    genre_total_plays = {}  # 각 장르의 총 재생 횟수를 저장
    genre_songs = {}  # 각 장르별로 (재생 횟수, 고유 번호) 튜플 리스트를 저장
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        # 장르별 총 재생 횟수를 누적
        genre_total_plays[genre] = genre_total_plays.get(genre, 0) + play
        # 각 장르별 노래 정보를 저장
        genre_songs[genre] = genre_songs.get(genre, []) + [(play, i)]
    
    # 총 재생 횟수에 따라 장르를 내림차순 정렬
    sorted_genre = sorted(genre_total_plays.items(), key=lambda x:x[1], reverse=True)
    
    answer = []
    # 정렬된 장르 순서대로 순회
    for genre, _ in sorted_genre:
        # 각 장르 내에서 노래들을 재생 횟수에 따라 내림차순으로 정렬 : -x[0]
        # 재생 횟수가 같은 경우 고유 번호가 낮은 노래가 우선순위 : x[1]
        sorted_songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        # 정렬된 노래 중 최대 2곡을 선택 후 answer 리스트에 추가
        answer.extend([song[1] for song in sorted_songs[:2]])
    
    return answer