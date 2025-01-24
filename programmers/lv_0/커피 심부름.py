def solution(order):
    return sum([5000 if 'latte' in drink else 4500 for drink in order])
