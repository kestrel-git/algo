def solution(arr, idx):
    # for i in range(idx, len(arr)):
    #     if arr[i]:
    #         return i
    # return -1

    try:
        return arr.index(1, idx)
    except:
        return -1
