def solution(picture, k):
    answer = []
    
    for row in picture:
        # 한 행을 기준으로 확대한 문자열 만들기
        new_row = ''.join(c * k for c in row)
          
        # 결과 리스트에 확대 개수만큼 추가
        for _ in range(k):
            answer.append(new_row)
    
    return answer
