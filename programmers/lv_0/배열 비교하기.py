def solution(arr1, arr2):
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    
    if len_arr1 != len_arr2:
        return 1 if len_arr1 > len_arr2 else -1
    else:
        sum_arr1 = sum(arr1)
        sum_arr2 = sum(arr2)
        if sum_arr1 == sum_arr2:
            return 0
        else:
            return 1 if sum_arr1 > sum_arr2 else -1
