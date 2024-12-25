def solution(sides):
    max_side = max(sides)
    return 1 if sum(sides) - max_side > max_side else 2
