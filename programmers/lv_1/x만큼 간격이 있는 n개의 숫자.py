def solution(x, n):
    if x != 0:
        k = 1 if x > 0 else -1
        return list(range(x, x * n + k, x))
    else:
        return [x] * n
