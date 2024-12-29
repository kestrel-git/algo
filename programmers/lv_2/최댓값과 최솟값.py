def solution(s):
    numbers = list(map(int, s.split()))
    return ' '.join([str(min(numbers)), str(max(numbers))])
