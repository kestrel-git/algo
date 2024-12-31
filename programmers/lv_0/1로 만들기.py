import math

def solution(num_list):
    return sum([int(math.log2(num)) for num in num_list])
