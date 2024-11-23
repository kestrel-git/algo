# 입력
scores_input = [list(map(int, input().split())) for _ in range(5)]

# 참가자별 점수 초기화
scores_sum = [0 for _ in range(5)]
max_cook_num = 0
max_cook_sum = 0

# 계산
for cur_cook_num, scores in enumerate(scores_input):
    cur_sum = sum(scores)
    if max_cook_sum < cur_sum:
        max_cook_sum = cur_sum
        max_cook_num = cur_cook_num

# 출력
print(max_cook_num + 1, max_cook_sum)
