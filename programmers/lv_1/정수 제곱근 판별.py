def solution(n):
    sq = n ** (1/2)
    return (sq + 1) ** 2 if sq.is_integer() else -1
