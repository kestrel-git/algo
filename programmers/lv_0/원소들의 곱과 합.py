import math

def solution(num_list):
    return int(math.prod(num_list) < pow(sum(num_list), 2))
