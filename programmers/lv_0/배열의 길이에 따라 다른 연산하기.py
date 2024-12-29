def solution(arr, n):
    st_idx = 0
    len_arr = len(arr)
    
    if not len_arr % 2:
        st_idx = 1
    
    for idx in range(st_idx, len_arr, 2):
        arr[idx] += n
        
    return arr
