def solution(score):
    # 평균 점수 계산. 2로 나누지 않아도 등수 계산이 가능하므로 점수 합계만 계산함
    avg_scores = list(map(sum, score))
    
    # 점수가 높은 순서로 정렬
    sorted_scores = sorted(avg_scores, reverse=True)
    
    # 점수와 등수 매핑
    rank_map = {}
    for rank, score in enumerate(sorted_scores, start=1):
        if score not in rank_map:  # 동점자의 경우 동일 등수로 지정
            rank_map[score] = rank
    
    # 결과 반환
    return [rank_map[a] for a in avg_scores]
