import math

def solution(n):
    cnt = 0
    sq = math.sqrt(n)
    for i in range(1, math.ceil(sq)):
        if n % i == 0:
            cnt += 1
    return cnt * 2 + int(sq.is_integer())
