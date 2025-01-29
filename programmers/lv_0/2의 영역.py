def solution(arr):
    if 2 not in arr:
        return [-1]
    else:
        st, ed = len(arr), 0
        for i, num in enumerate(arr):
            if num == 2:
                st = min(st, i)
                ed = max(st, i)
        return arr[st:ed+1]
