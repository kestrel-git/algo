def solution(arr, k):
    res = []
    for num in arr:
        if len(res) >= k:
            break
        if num not in res:
            res.append(num)
    return res + ([-1] * (k - len(res)))
