import math

def solution(n):
    answer = [1, n]
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            answer += [i, n/i]
    
    return sorted(set(answer))
