def solution(n, slicer, num_list):
    if n == 1:
        slicer[0] = 0
        slicer[2] = 1
    elif n == 2:
        slicer[1] = len(num_list)
        slicer[2] = 1
    elif n == 3:
        slicer[2] = 1
        
    return num_list[slicer[0] : slicer[1]+1 : slicer[2]]
