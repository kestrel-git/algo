def solution(numbers):
    max_num = max(numbers)
    numbers.remove(max_num)
    return max_num * max(numbers)
