def solution(arr):
    stk = []
    
    for i in range(len(arr)):
        if not stk or stk[-1] != arr[i]:
            stk.append(arr[i])
        else:
            stk.pop()
    
    return stk or [-1]
