def solution(num_list):
    res = [0, 0]
    for num in num_list:
        res[num % 2] += 1
    return res
