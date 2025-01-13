def solution(a, b, c):
    num_len = len(set([a, b, c]))
    res = (a + b + c)
    
    if num_len == 2:
        res *= (a**2 + b**2 + c**2)
    elif num_len == 1:
        res *= (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
        
    return res
