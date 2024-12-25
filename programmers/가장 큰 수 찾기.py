def solution(array):
    max_idx = 0
    max_num = array[max_idx]
    
    for idx in range(1, len(array)):
        if array[idx] > max_num:
            max_idx = idx
            max_num = array[max_idx]
            
    return [max_num, max_idx]
