import math

def solution(n):
    k = n - 1
    
    for i in range(2, int(math.sqrt(k)) + 1):
        if k % i == 0:
            return i

    return k
