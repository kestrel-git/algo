def solution(price, money, count):
    total = price * count * (count + 1) / 2
    return total - money if total > money else 0  # return max(0, total - money)
