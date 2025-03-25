def gcd(a, b):
    if a < b:  # 큰 수를 a, 작은 수를 b로 설정
        a, b = b, a
    
    while b:   # 작은 수로 큰 수를 나눈 나머지가 0이 될 때까지 반복
        a, b = b, a % b
    
    return a


def lcm(a, b, g=None):
    return a * b // (g or gcd(a, b))
    

def solution(n, m):
    g = gcd(n, m)
    return [g, lcm(n, m, g)]
