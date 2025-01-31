import math

def solution(box, n):
    return math.prod(map(lambda l: l//n, box))
