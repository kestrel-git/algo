import math

def solution(left, right):
    res = 0
    for n in range(left, right+1):
        if math.sqrt(n).is_integer():  # 홀수 개 (정수로 떨어지므로)
            res -= n
        else:  # 짝수 개
            res += n
    return res
