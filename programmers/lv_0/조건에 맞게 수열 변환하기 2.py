def solution(arr):
    x = 0
    prev_arr = []
    
    while prev_arr != arr:
        x += 1
        prev_arr = arr.copy()
        
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] /= 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i] * 2 + 1
    
    return x - 1
