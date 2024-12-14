def solution(n, control):
    con_num = {"w": 1, "s": -1, "d": 10, "a": -10}
    return n + sum([con_num[c] for c in control])
