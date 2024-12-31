def solution(n):
    res = []
    for idx in range(n):
        row = [0] * n
        row[idx] = 1
        res.append(row)
    return res
