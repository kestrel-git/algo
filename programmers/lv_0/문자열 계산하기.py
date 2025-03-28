def solution(my_string):
    arr = my_string.split()
    res = int(arr[0])
    
    for i in range(1, len(arr), 2):
        if arr[i] == '+':
            res += int(arr[i+1])
        else:
            res -= int(arr[i+1])
            
    return res
    
    # return eval(my_string)
