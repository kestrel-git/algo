import math

def solution(arr):
    arr_len = len(arr)
    res_len = 2 ** math.ceil(math.log2(arr_len))
    return arr + [0] * (res_len - arr_len)
