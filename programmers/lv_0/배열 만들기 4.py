def solution(arr):
    stk = []
    i, len_arr = 0, len(arr)
    
    while i < len_arr:
        if not stk or stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        else:
            stk.pop()
    
    return stk
