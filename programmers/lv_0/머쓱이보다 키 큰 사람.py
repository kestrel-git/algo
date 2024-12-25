def solution(array, height):
    return sum([1 for f_height in array if f_height > height])
