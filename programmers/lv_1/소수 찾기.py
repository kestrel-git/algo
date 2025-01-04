def solution(n):
    numbers = dict.fromkeys(range(2, n+1))
    for num in range(2, int(n ** 1/2) + 1):
        if num in numbers:
            for k in range(num*2, n+1, num):
                numbers.pop(k, None)
    return len(numbers.keys())
