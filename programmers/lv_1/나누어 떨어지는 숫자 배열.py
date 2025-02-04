def solution(arr, divisor):
    answer = [n for n in arr if n % divisor == 0] or [-1]
    return sorted(answer)
