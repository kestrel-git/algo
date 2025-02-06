import math

def solution(n):
    res = 0
    sq = math.sqrt(n)
    
    for i in range(1, math.ceil(sq)):
        if n % i == 0:
            res += i + n/i
    
    if sq.is_integer():
        res += sq
    
    return res
