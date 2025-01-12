def solution(a, d, included):
    res = 0
    for idx, flag in enumerate(included):
        res += (a + d * idx) * int(flag)
    return res
