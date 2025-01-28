def solution(board, k):
    res = 0
    for i, r_arr in enumerate(board):
        for j, num in enumerate(r_arr):
            if i + j <= k:
                res += num
            else:
                break
    return res
