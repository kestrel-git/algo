def solution(arr, k):
    if k % 2:
        return [num * k for num in arr]
    else:
        return [num + k for num in arr]
