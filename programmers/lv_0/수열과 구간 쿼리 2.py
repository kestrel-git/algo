def solution(arr, queries):
    res = []
    for s, e, k in queries:
        res.append(min([n for n in arr[s:e+1] if n > k] or [-1]))
    return res
