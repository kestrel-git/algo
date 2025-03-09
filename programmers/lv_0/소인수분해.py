def solution(n):
    factors = []
    d = 2
    
    while d * d <= n:          # n의 제곱근까지만 계산
        if n % d == 0:
            factors.append(d)  # 소인수 추가
            while n % d == 0:  # 해당 소인수 중복 방지
                n /= d
        d += 1  # 다음 숫자
    
    if n > 1:   # 1보다 크면 n도 소인수 (소인수가 아니라면 위에서 계속 나눠지며 1이 되었을 것)
        factors.append(n)
    
    return sorted(factors)
