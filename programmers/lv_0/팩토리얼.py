def solution(n):
    f, k = 1, 1
    
    while f <= n:
        k += 1
        f *= k
    
    return k - 1
