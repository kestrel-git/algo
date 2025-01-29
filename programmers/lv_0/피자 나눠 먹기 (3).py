def solution(slice, n):
    d, m = divmod(n, slice)
    return d + int(m != 0)
