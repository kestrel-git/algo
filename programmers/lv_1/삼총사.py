from itertools import combinations

def solution(number):
    return sum(1 for trio in combinations(number, 3) if sum(trio) == 0)
