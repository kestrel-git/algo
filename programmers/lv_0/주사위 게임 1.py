def solution(a, b):
    if a % 2 and b % 2:  # 모두 홀수
        return a ** 2 + b ** 2
    elif not a % 2 and not b % 2:  # 모두 짝수
        return abs(a - b)
    else:  # 둘 중 하나만 홀수
        return 2 * (a + b)
