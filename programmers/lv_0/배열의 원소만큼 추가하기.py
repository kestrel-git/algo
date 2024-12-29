def solution(arr):
    res = []
    for num in arr:
        res += [num] * num
    return res
